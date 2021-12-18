import re
import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')


def reduce_line(line):
    reduced = explode_line(line)
    reduced = split_line(reduced)

    if reduced != line:
        return reduce_line(reduced)

    return reduced


def explode_line(line):
    max_level = 0
    max_level_start_pos = 0
    current_level = 0

    for pos in range(len(line)):
        if line[pos: pos + 1] == '[':
            current_level += 1
        elif line[pos: pos + 1] == ']':
            current_level -= 1

        if current_level > max_level:
            max_level = current_level
            max_level_start_pos = pos

    if max_level < 5:
        return line

    out_line = ''
    max_pair_str = line[max_level_start_pos:]
    max_pair_length = max_pair_str.index(']')
    max_pair_str = max_pair_str[:max_pair_length + 1]
    max_first_digit, max_last_digit = map(int, max_pair_str[1:len(max_pair_str) - 1].split(','))

    prev_number_start = None
    for distance in range(max_level_start_pos):
        check_char_pos = max_level_start_pos - distance
        check_char = line[check_char_pos - 1:check_char_pos]

        if prev_number_start is None and check_char not in [',', '[', ']']:  # if it's a number
            prev_number_start = check_char_pos - 1
        elif prev_number_start is not None:
            if check_char in [',', '[', ']']:
                break
            else:
                prev_number_start = check_char_pos - 1

    if prev_number_start is None:
        out_line = line[:max_level_start_pos] + '0'
    else:
        out_line = line[:prev_number_start]
        prev_number = int(re.compile(r'[0-9]+').search(line[prev_number_start:])[0])

        out_line += str(max_first_digit + prev_number)
        out_line += line[prev_number_start + len(str(prev_number)):max_level_start_pos]

    next_number_start = None
    for distance in range(len(line) - (max_level_start_pos + max_pair_length)):
        check_char_pos = max_level_start_pos + max_pair_length + distance
        check_char = line[check_char_pos:check_char_pos + 1]

        if next_number_start is None and check_char not in [',', '[', ']']:  # if it's a number
            next_number_start = check_char_pos
            break

    if next_number_start is None:
        out_line += '0' + line[max_level_start_pos + max_pair_length + 1:]
    else:
        next_number = int(re.compile(r'[0-9]+').search(line[next_number_start:])[0])
        if prev_number_start is not None:
            out_line += '0'
        out_line += line[max_level_start_pos + max_pair_length + 1:next_number_start]
        out_line += str(next_number + max_last_digit)
        out_line += line[next_number_start + len(str(next_number)):]

    return explode_line(out_line)


def split_line(line):
    first_split_match = re.compile(r'[0-9]{2,}').search(line)

    if first_split_match is None:
        return line

    start, end = first_split_match.span()
    number = int(first_split_match.group())

    split_base = int(number / 2)

    return f'{line[:start]}[{split_base},{number - split_base}]{line[end:]}'


def calc_magnitude(line):
    pair_matcher = re.compile(r'\[([0-9]+),([0-9]+)\]')

    outline = line

    while True:
        pair = pair_matcher.search(outline)

        if pair is None:
            break

        a, b = map(int, pair.groups())

        outline = outline[:pair.start()] + str((3 * a) + (2 * b)) + outline[pair.end():]

    return outline


def sum_lines(a, b):
    return f'[{a},{b}]'


lines = open(input_file, 'r').read().strip().split('\n')
line_sum = lines[0]

for line_number in range(1, len(lines)):
    line_sum = reduce_line(sum_lines(line_sum, lines[line_number]))

print('part 1:', calc_magnitude(line_sum))

max_sum = 0
for line_number in range(len(lines)):
    for add_line_number in range(len(lines)):
        if line_number != add_line_number:
            line_sum = int(
                calc_magnitude(
                    reduce_line(
                        sum_lines(lines[line_number], lines[add_line_number])
                    )
                )
            )

            if line_sum > max_sum:
                max_sum = line_sum

print('part 2:', max_sum)
