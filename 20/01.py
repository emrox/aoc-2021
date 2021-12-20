import os
from collections import Counter
from typing import Sequence

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

algorythm, raw_image = open(input_file, 'r').read().strip().split('\n\n')

base_image = raw_image.split('\n')
base_blank_pixel = algorythm[-1]

def pixel_sequence_to_new_pixel(sequence):
    binary_calc_string = sequence.replace('.', '0').replace('#', '1')
    calc_pos = int(binary_calc_string, 2)
    return algorythm[calc_pos:calc_pos + 1]


def calc_pixel(img, x, y):
    pixel_calc_string= ''
    line_count = len(img)
    line_length = len(img[0])

    pixel_calc_string = (
        (img[y - 1][x - 1] if y > 0 and x > 0 else base_blank_pixel) +
        (img[y - 1][x] if y > 0 else base_blank_pixel) +
        (img[y - 1][x + 1] if y > 0 and x < (line_length - 1) else base_blank_pixel) +
        (img[y][x - 1] if x > 0 else base_blank_pixel) +
        img[y][x] +
        (img[y][x + 1] if x < (line_length - 1) else base_blank_pixel) +
        (img[y + 1][x - 1] if (y < (line_count - 1)) and x > 0 else base_blank_pixel) +
        (img[y + 1][x] if (y < (line_count - 1)) else base_blank_pixel) +
        (img[y + 1][x + 1] if (y < (line_count - 1)) and x < (line_length - 1) else base_blank_pixel)
    )

    return pixel_sequence_to_new_pixel(pixel_calc_string)

def expand_image(img):
    blank_line = [base_blank_pixel]*(len(img[0]) + 2)

    expanded_img = [blank_line.copy()]

    for line in img:
        expanded_img.append([base_blank_pixel, *line, base_blank_pixel])

    expanded_img.append(blank_line.copy())

    return expanded_img


iterations = 50

for iteration in range(iterations):
    base_image = expand_image(base_image)
    new_image = []

    for y in range(len(base_image)):
        new_line = []

        for x in range(len(base_image[0])):
            new_line.append(calc_pixel(base_image, x, y))

        new_image.append(new_line)

    base_image = new_image
    base_blank_pixel = pixel_sequence_to_new_pixel(9 * base_blank_pixel)

print(''.join(map(lambda l: ''.join(l), base_image)).count('#'))
