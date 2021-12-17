import re

input = 'target area: x=150..171, y=-129..-70'
# input = 'target area: x=20..30, y=-10..-5'

x_from, x_to, y_to, y_from = map(
    int,
    re.search(r'x=([0-9\-]+)\.\.([0-9\-]+), y=([0-9\-]+)\.\.([0-9\-]+)', input).groups()
)

positive_probes = []
valid_velocities = []

for x_vel in range((x_to * 2) + 1):
    for y_vel in range((abs(y_to) * 2) + 1):
        current_velocity = [0 - x_to + x_vel, 0 - abs(y_to) + y_vel]
        next_velocity = current_velocity.copy()
        probe_positions = []

        while True:
            new_probe_position = probe_positions[-1].copy() if len(probe_positions) > 0 else [0, 0]
            new_probe_position[0] += next_velocity[0]
            new_probe_position[1] += next_velocity[1]

            probe_positions.append(new_probe_position)

            if next_velocity[0] > 0:
                next_velocity[0] -= 1
            elif next_velocity[0] < 0:
                next_velocity[0] += 1
            else:
                next_velocity[0] = 0

            next_velocity[1] -= 1

            if (new_probe_position[0] > x_to or next_velocity[0] == 0) and new_probe_position[1] <= y_to:
                break

        for probe_position in probe_positions:
            x, y = probe_position

            if x >= x_from and x <= x_to and y <= y_from and y >= y_to:
                positive_probes.append(probe_positions)
                valid_velocities.append(current_velocity)
                break

max_y = 0
for probe_nr, positive_probe in enumerate(positive_probes):
    probe_max_y = max(list(map(lambda p: p[1], positive_probe)))

    max_y = probe_max_y if probe_max_y > max_y else max_y

print(f'Maximum Y Pos: {max_y}, valid Velocities: {len(valid_velocities)}')
