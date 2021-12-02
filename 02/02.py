import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '02.input'

with open(base_directory + '/' + input_file) as file:
    input_lines = list(map(str.strip, file.readlines()))

position = [0, 0]
aim = 0

for line in input_lines:
    direction, raw_value = line.split(' ')
    value = int(raw_value)

    if direction == 'forward':
        position[0] += value
        position[1] += value * aim

    if direction == 'up':
        aim -= value

    if direction == 'down':
        aim += value

print(position, aim, position[0] * position[1])
