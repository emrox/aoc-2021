import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

raw_coordinates, fold_instructions = map(
    lambda line: line.split('\n'),
    open(input_file, 'r').read().strip().split('\n\n')
)

coordinates = []
sheet = []
max_x = 0
max_y = 0
first_fold_dot_count = 0

# prepare coordinates, get max dimensions
for raw_coordinate in raw_coordinates:
    x, y = list(map(int, raw_coordinate.split(',')))

    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y

    coordinates.append([x, y])

# prepare sheet
for _ in range(max_y + 1):
    sheet.append([False]*(max_x + 1))

for coordinate in coordinates:
    sheet[coordinate[1]][coordinate[0]] = True

# fold
for fold_instruction in fold_instructions:
    direction, position = list(map(lambda i: i.split('='), fold_instruction.split(' ')))[2]
    position = int(position)

    new_sheet = []
    line_count = len(sheet)

    if direction == 'y':
        for _ in range(abs(len(sheet) - position) - 1):
            new_sheet.append([False]*len(sheet[0]))

        for y in range(line_count):
            target_y = y if y < position else position - y

            for x in range(len(sheet[0])):
                if sheet[y][x] is True:
                    new_sheet[target_y][x] = True
    else:
        new_line_length = position

        for y in range(line_count):
            new_line = [False]*new_line_length

            for x in range(len(sheet[0])):
                if sheet[y][x] is True:
                    if x < position:
                        new_line[x] = True
                    else:
                        new_line[position - x] = True

            new_sheet.append(new_line)

    sheet = new_sheet

    if first_fold_dot_count == 0:
        for line in sheet:
            first_fold_dot_count += line.count(True)

print('first_fold_dot_count:', first_fold_dot_count)
print()

for line in sheet:
    print(''.join(list(map(lambda c: ' ' if c is False else '#', line))))
