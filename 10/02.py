import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

lines = open(input_file, 'r').read().strip().split('\n')

chunk_mapping = [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]
chunk_openings = list(map(lambda chunk: chunk[0], chunk_mapping))

all_line_points = []

for line in lines:
    is_corrupt = False
    chunk_stack = []
    line_points = 0

    for character in line:
        if character in chunk_openings:
            chunk_stack.append(chunk_mapping[chunk_openings.index(character)])
        else:
            if character != chunk_stack[-1][1]:
                is_corrupt = True
                continue

            chunk_stack.pop()

    if is_corrupt is True:
        continue

    if len(chunk_stack) == 0:
        continue

    chunk_stack.reverse()

    for autocomplete_chunk in chunk_stack:
        line_points = line_points * 5

        if autocomplete_chunk[1] == ')':
            line_points += 1

        if autocomplete_chunk[1] == ']':
            line_points += 2

        if autocomplete_chunk[1] == '}':
            line_points += 3

        if autocomplete_chunk[1] == '>':
            line_points += 4

    all_line_points.append(line_points)

all_line_points.sort()

print(all_line_points[int(len(all_line_points) / 2)])
