import os
from collections import Counter

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

template, raw_instructions = open(input_file, 'r').read().strip().split('\n\n')

instructions = {}

for instruction in raw_instructions.split('\n'):
    target, insertion = instruction.split(' -> ')

    if target in instructions:
        print(f'duplicate instruction for {target}')

    instructions[target] = insertion

for step in range(10):
    new_template = ''

    for pair_pos in range(len(template) - 1):
        pair = template[pair_pos:pair_pos + 2]

        new_template += template[pair_pos:pair_pos + 1]

        if pair in instructions:
            new_template += instructions[pair]

    new_template += template[len(template) - 1:len(template)]

    template = new_template

collection = Counter(template).most_common()

print(collection[0][1] - collection[-1][1])
