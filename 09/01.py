import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')


def numbers_to_int(line):
    return list(map(int, line))


lines = list(map(numbers_to_int, open(input_file, 'r').read().strip().split('\n')))
line_count = len(lines)

low_numbers = []

for row_number, row in enumerate(lines):
    row_length = len(row)

    for column_number, number in enumerate(row):
        is_low_number = True

        if row_number > 0 and number >= lines[row_number - 1][column_number]:
            is_low_number = False

        if row_number < (line_count - 1) and number >= lines[row_number + 1][column_number]:
            is_low_number = False

        if column_number > 0 and number >= lines[row_number][column_number - 1]:
            is_low_number = False

        if column_number < (row_length - 1) and number >= lines[row_number][column_number + 1]:
            is_low_number = False

        if is_low_number is True:
            low_numbers.append(number)

print(sum(low_numbers) + len(low_numbers))
