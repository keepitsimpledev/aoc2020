import unittest

from aoc_util import get_lines
from aoc_util import assert_with_message


def calculate_row(code: str):
    assert len(code) == 10
    code = code.replace('F', '0')
    code = code.replace('B', '1')
    return int(code[0:7], 2)


def calculate_column(code: str):
    assert len(code) == 10
    code = code.replace('L', '0')
    code = code.replace('R', '1')
    return int(code[7:10], 2)


def calculate_seat_id(code: str):
    return (8 * calculate_row(code)) + calculate_column(code)


def generate_seatmap():
    seatmap = []
    for i in range(128):
        row = [0, 0, 0, 0, 0, 0, 0, 0]
        seatmap = seatmap + [row]
    return seatmap


def mark_seatmap(seatmap, code):
    row = calculate_row(code)
    column = calculate_column(code)
    seatmap[row][column] = code


def is_my_seat(seatmap, row, column):
    if 0 < row < len(seatmap) :
        previous_row = row if column > 0 else row - 1
        previous_column = column - 1 if column > 0 else 7
        next_row = row if column < 7 else row + 1
        next_column = column + 1 if column < 7 else 0
        if seatmap[previous_row][previous_column] != 0 != seatmap[next_row][next_column]:
            return [row, column]
    return None


def part2():
    codes = get_lines('day5.input')
    seatmap = generate_seatmap()
    for code in codes:
        mark_seatmap(seatmap, code)
    for row in range(len(seatmap)):
        for column in range(len(seatmap[row])):
            if seatmap[row][column] == 0 and is_my_seat(seatmap, row, column):
                print('my seat is row {} column {}.'.format(row, column))


def assert_row_column_seatid(code: str, row, column, seat_id):
    assert_with_message(row, calculate_row(code))
    assert_with_message(column, calculate_column(code))
    assert_with_message(seat_id, calculate_seat_id(code))


class TestStringMethods(unittest.TestCase):

    def test_part2(self):
        assert_row_column_seatid('FBFBBFFRLR', 44, 5, 357)
        assert_row_column_seatid('BFFFBBFRRR', 70, 7, 567)
        assert_row_column_seatid('FFFBBBFRRR', 14, 7, 119)
        assert_row_column_seatid('BBFFBBFRLL', 102, 4, 820)

        part2()
