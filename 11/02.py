import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')


def numbers_to_int(line):
    return list(map(int, line))


lines = list(map(numbers_to_int, open(input_file, 'r').read().strip().split('\n')))
steps = 0

line_count = len(lines)
line_lengh = len(lines[0])
required_flash_count = line_count * line_lengh


def increase(row, col):
    lines[row][col] += 1

    if lines[row][col] == 10:
        explode(row, col)


def explode(row, col):
    if row > 0:
        if col > 0:
            lines[row - 1][col - 1] += 1
            if lines[row - 1][col - 1] == 10:
                explode(row - 1, col - 1)

        lines[row - 1][col] += 1
        if lines[row - 1][col] == 10:
            explode(row - 1, col)

        if col < line_lengh - 1:
            lines[row - 1][col + 1] += 1
            if lines[row - 1][col + 1] == 10:
                explode(row - 1, col + 1)

    if col > 0:
        lines[row][col - 1] += 1
        if lines[row][col - 1] == 10:
            explode(row, col - 1)

    lines[row][col] += 1
    if lines[row][col] == 10:
        explode(row, col)

    if col < line_lengh - 1:
        lines[row][col + 1] += 1
        if lines[row][col + 1] == 10:
            explode(row, col + 1)

    if row < line_count - 1:
        if col > 0:
            lines[row + 1][col - 1] += 1
            if lines[row + 1][col - 1] == 10:
                explode(row + 1, col - 1)

        lines[row + 1][col] += 1
        if lines[row + 1][col] == 10:
            explode(row + 1, col)

        if col < line_lengh - 1:
            lines[row + 1][col + 1] += 1
            if lines[row + 1][col + 1] == 10:
                explode(row + 1, col + 1)


while True:
    steps += 1
    flash_count = 0

    for row in range(line_count):
        for col in range(line_lengh):
            increase(row, col)

    for row in range(line_count):
        for col in range(line_lengh):
            if lines[row][col] > 9:
                flash_count += 1
                lines[row][col] = 0

    if flash_count == required_flash_count:
        break

print(steps)
