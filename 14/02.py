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

pairs = {}

for pair_pos in range(len(template) - 1):
    pair = template[pair_pos:pair_pos + 2]

    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

for step in range(40):
    new_pairs = {}

    for pair in iter(pairs):
        add_pairs = [pair]

        if pair in instructions:
            add_pairs = [
                pair[0] + instructions[pair],
                instructions[pair] + pair[1]
            ]

        for add_pair in add_pairs:
            pair_occ = pairs[pair] if pair in pairs else 1

            if add_pair in new_pairs:
                new_pairs[add_pair] += pair_occ
            else:
                new_pairs[add_pair] = pair_occ

    pairs = new_pairs

first_letter = list(pairs)[0]
letter_counts = {
    first_letter[0]: 1
}

for pair in iter(pairs):
    letter = pair[1]

    if letter in letter_counts:
        letter_counts[letter] += pairs[pair]
    else:
        letter_counts[letter] = pairs[pair]

collection = Counter(letter_counts).most_common()

print(collection[0][1] - collection[-1][1])
