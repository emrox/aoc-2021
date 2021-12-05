import os

from functools import reduce

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')


def input_to_vents(input):
    return [list(map(int, position.split(','))) for position in input.strip().split(' -> ')]


def compute_map_size(map_size, positions):
    position_max = max(set(positions[0] + positions[1]))

    return position_max if position_max > map_size else map_size


def init_vent_map(map_size):
    vent_map = []

    for _x in range(map_size + 1):
        vent_map.append([0]*(map_size + 1))

    return vent_map


vents = [input_to_vents(line) for line in open(input_file, 'r').read().strip().split('\n')]
map_size = reduce(compute_map_size, vents, 0)
vent_map = init_vent_map(map_size)

for vent in vents:
    # vertical
    if vent[0][0] == vent[1][0]:
        start_pos = vent[0][1] if vent[0][1] <= vent[1][1] else vent[1][1]

        for step in range(abs(vent[0][1] - vent[1][1]) + 1):
            vent_map[start_pos + step][vent[0][0]] += 1

    # horizontal
    if vent[0][1] == vent[1][1]:
        start_pos = vent[0][0] if vent[0][0] <= vent[1][0] else vent[1][0]

        for step in range(abs(vent[0][0] - vent[1][0]) + 1):
            vent_map[vent[0][1]][start_pos + step] += 1

overlapping_count = reduce(lambda result, line: result + len(list(filter(lambda count: count >= 2, line))), vent_map, 0)

print(overlapping_count)
