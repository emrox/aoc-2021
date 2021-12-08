import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

digit_sum = 0

for line in open(input_file, 'r').read().strip().split('\n'):
    patterns, output_digits = line.split(' | ')

    patterns = list(map(sorted, patterns.split(' ')))
    output_digits = list(map(sorted, output_digits.split(' ')))
    len_patterns = sorted(patterns, key=len)

    segment = ['-']*7
    number_patterns = [None]*10

    segment[0] = list(filter(lambda n: n not in len_patterns[0], len_patterns[1]))[0]

    # simple things first
    number_patterns[1] = len_patterns[0]
    number_patterns[4] = len_patterns[2]
    number_patterns[7] = len_patterns[1]
    number_patterns[8] = len_patterns[9]

    # six
    for six_candidate in len_patterns[6:9]:
        filtered_six_candidate = list(filter(lambda n: n not in six_candidate, len_patterns[1]))

        if len(filtered_six_candidate) == 1:
            segment[2] = filtered_six_candidate[0]
            number_patterns[6] = six_candidate
            break

    # five
    for five_candidate in len_patterns[3:6]:
        if segment[2] not in five_candidate:
            number_patterns[5] = five_candidate
            segment[4] = list(filter(lambda n: n not in five_candidate, number_patterns[6]))[0]
            break

    # nine
    for nine_candidate in len_patterns[6:9]:
        if nine_candidate != number_patterns[6] and segment[4] not in nine_candidate:
            number_patterns[9] = nine_candidate
            break

    # zero
    for zero_candidate in len_patterns[6:9]:
        if zero_candidate != number_patterns[6] and zero_candidate != number_patterns[9]:
            number_patterns[0] = zero_candidate
            segment[3] = list(filter(lambda n: n not in zero_candidate, number_patterns[8]))[0]
            break

    # three
    for three_candidate in len_patterns[3:6]:
        if three_candidate != number_patterns[5] and segment[4] not in three_candidate:
            number_patterns[3] = three_candidate
            break

    # two
    for two_candidate in len_patterns[3:6]:
        if two_candidate != number_patterns[5] and two_candidate != number_patterns[3]:
            number_patterns[2] = two_candidate
            break

    shown_digits = ''

    for output_digit in output_digits:
        shown_digits += str(number_patterns.index(output_digit))

    digit_sum += int(shown_digits)

print(digit_sum)
