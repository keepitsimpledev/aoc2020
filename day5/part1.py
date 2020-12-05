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


def part1():
    codes = get_lines('day5.input')
    high = 0
    for code in codes:
        if high < calculate_seat_id(code):
            high = calculate_seat_id(code)
    print('high is {}'.format(high))


def assert_row_column_seatid(code: str, row, column, seat_id):
    assert_with_message(row, calculate_row(code))
    assert_with_message(column, calculate_column(code))
    assert_with_message(seat_id, calculate_seat_id(code))


class TestStringMethods(unittest.TestCase):

    def test_part1(self):
        assert_row_column_seatid('FBFBBFFRLR', 44, 5, 357)
        assert_row_column_seatid('BFFFBBFRRR', 70, 7, 567)
        assert_row_column_seatid('FFFBBBFRRR', 14, 7, 119)
        assert_row_column_seatid('BBFFBBFRLL', 102, 4, 820)

        part1()
