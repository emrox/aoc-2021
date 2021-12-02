import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '02.input'

with open(base_directory + '/' + input_file) as file: input_lines = list(map(str.strip, file.readlines()))

position = [0, 0]

for line in input_lines:
  direction, raw_value = line.split(' ')
  value = int(raw_value)

  if direction == 'forward':
    position[0] += value
  
  if direction == 'up':
    position[1] -= value
  
  if direction == 'down':
    position[1] += value

print(position, position[0] * position[1])