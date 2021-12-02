import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '01.input'

with open(base_directory + '/' + input_file) as file:
    input_lines = list(map(str.strip, file.readlines()))

increases = 0
last_window_sum = None
measurement_window = []
max_measurement_window_size = 3

for line in input_lines:
    depth = int(line)

    measurement_window.append(depth)

    if len(measurement_window) >= max_measurement_window_size:
        if len(measurement_window) > max_measurement_window_size:
            measurement_window.pop(0)

        measurement_window_sum = sum(measurement_window)
        print(measurement_window, measurement_window_sum)

        if last_window_sum is not None and measurement_window_sum > last_window_sum:
            increases += 1

        last_window_sum = measurement_window_sum

print(increases)
