import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '01.input'

with open(base_directory + '/' + input_file) as file: input_lines = list(map(str.strip, file.readlines()))

increases = 0
last_depth = int(input_lines[0])

for line in input_lines:
  depth = int(line)

  if depth > last_depth:
    increases += 1

  last_depth = depth

print(increases)
