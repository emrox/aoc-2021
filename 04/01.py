import os
import re

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '04.input'

with open(os.path.join(base_directory, input_file)) as file:
    input_lines = [line.strip() for line in file.readlines()]

#  get draw numbers
draw_numbers = list(map(int, input_lines[0].split(',')))

input_lines = input_lines[2:]

# get boards
boards = [[]]
match_boards = [[[False]*5, [False]*5, [False]*5, [False]*5, [False]*5]]
number_matcher = re.compile(r'\d+')

for input_line in input_lines:
    if input_line == '':
        boards.append([])
        match_boards.append([[False]*5, [False]*5, [False]*5, [False]*5, [False]*5])
    else:
        board_line_numbers = list(map(int, number_matcher.findall(input_line)))
        boards[-1].append(board_line_numbers)

bingo_number = None
winning_board = None

# find bingo
for draw_number in draw_numbers:
    # fill match board
    for board_index, board in enumerate(boards):
        for board_line_number, board_line in enumerate(board):
            draw_number_index = board_line.index(draw_number) if draw_number in board_line else None

            if draw_number_index is not None:
                match_boards[board_index][board_line_number][draw_number_index] = True

    # find horizontal match
    for board_index, board in enumerate(match_boards):
        for board_line_number, board_line in enumerate(board):
            if board_line == [True]*5:
                bingo_number = draw_number
                winning_board = board_index
                break

    # find vertical match
    for board_index, board in enumerate(match_boards):
        for column in range(5):
            column_matches = []

            for row in range(5):
                column_matches.append(match_boards[board_index][row][column])

            if column_matches == [True]*5:
                bingo_number = draw_number
                winning_board = board_index
                break

    if bingo_number is not None:
        break

winning_board_numbers = sum(boards[winning_board], [])
left_winning_board_numbers = list(
    set(winning_board_numbers).difference(set(draw_numbers[:draw_numbers.index(bingo_number) + 1]))
)

print('winning board score: ' + str(sum(left_winning_board_numbers) * bingo_number))
