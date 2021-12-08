import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

simple_digits_occurrences = 0
simple_digit_mapping = [
    2,  # 1
    4,  # 4
    3,  # 7
    7,  # 8
]

for line in open(input_file, 'r').read().strip().split('\n'):
    patterns, output_values = line.split(' | ')

    patterns = patterns.split(' ')
    output_values = output_values.split(' ')

    output_value_lenghts = list(map(len, output_values))

    simple_digits_occurrences += len(list(filter(lambda length: length in simple_digit_mapping, output_value_lenghts)))

print(simple_digits_occurrences)
