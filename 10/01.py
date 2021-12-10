import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

lines = open(input_file, 'r').read().strip().split('\n')

chunk_mapping = [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]
chunk_openings = list(map(lambda chunk: chunk[0], chunk_mapping))

points = 0

for line in lines:
    chunk_stack = []

    for character in line:
        if character in chunk_openings:
            chunk_stack.append(chunk_mapping[chunk_openings.index(character)])
        else:
            if character != chunk_stack[-1][1]:
                if character == ')':
                    points += 3

                if character == ']':
                    points += 57

                if character == '}':
                    points += 1197

                if character == '>':
                    points += 25137

            chunk_stack.pop()

print(points)
