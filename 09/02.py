import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')


def numbers_to_int(line):
    return list(map(int, line))


def basin_bases(lines):
    line_count = len(lines)
    line_length = len(lines[0])
    basin_bases = []

    for row_number, row in enumerate(lines):
        for column_number, number in enumerate(row):
            is_low_number = True

            if row_number > 0 and number >= lines[row_number - 1][column_number]:
                is_low_number = False

            if row_number < (line_count - 1) and number >= lines[row_number + 1][column_number]:
                is_low_number = False

            if column_number > 0 and number >= lines[row_number][column_number - 1]:
                is_low_number = False

            if column_number < (line_length - 1) and number >= lines[row_number][column_number + 1]:
                is_low_number = False

            if is_low_number is True:
                basin_bases.append([row_number, column_number])

    return basin_bases


lines = list(map(numbers_to_int, open(input_file, 'r').read().strip().split('\n')))
line_count = len(lines)
line_length = len(lines[0])
basin_sizes = []

for basin_base in basin_bases(lines):
    known_basin_tiles = []
    check_for_neighbors = [basin_base]

    while len(check_for_neighbors) > 0:
        other_neighbors = []

        for tile in check_for_neighbors:
            if tile not in known_basin_tiles:
                known_basin_tiles.append(tile)

            candidates = []

            if tile[0] > 0 and lines[tile[0] - 1][tile[1]] < 9:
                candidates.append([tile[0] - 1, tile[1]])

            if tile[0] < (line_count - 1) and lines[tile[0] + 1][tile[1]] < 9:
                candidates.append([tile[0] + 1, tile[1]])

            if tile[1] > 0 and lines[tile[0]][tile[1] - 1] < 9:
                candidates.append([tile[0], tile[1] - 1])

            if tile[1] < (line_length - 1) and lines[tile[0]][tile[1] + 1] < 9:
                candidates.append([tile[0], tile[1] + 1])

            for candidate in candidates:
                if candidate not in known_basin_tiles:
                    other_neighbors.append(candidate)

        check_for_neighbors = other_neighbors

    basin_sizes.append(len(known_basin_tiles))

largest_basins = sorted(basin_sizes)[-3:]

print(largest_basins[0] * largest_basins[1] * largest_basins[2])
