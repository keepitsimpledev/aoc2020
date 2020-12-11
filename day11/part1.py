import unittest

from aoc_util import assert_with_message
from aoc_util import get_input


def get_num_occupied_after_updates(seating_chart):
    last = seating_chart
    current = update_seats(last.copy())
    while last != current:
        last = current
        current = update_seats(last.copy())
    num_occupied = 0
    for i in range(len(last)):
        for j in range(len(last[i])):
            if last[i][j] == '#':
                num_occupied += 1
    return num_occupied


def update_seats(seating_chart):
    to_update = []
    for i in range(len(seating_chart)):
        for j in range(len(seating_chart[i])):
            if seating_chart[i][j] == '.':
                continue
            if seating_chart[i][j] != '#' and count_occupied_adjacent_seats(i, j, seating_chart) == 0:
                to_update += [[i, j, '#']]
            elif seating_chart[i][j] == '#' and count_occupied_adjacent_seats(i, j, seating_chart) >= 4:
                to_update += [[i, j, 'L']]
    for item in to_update:
        row = seating_chart[item[0]]
        row = row[:item[1]] + item[2] + row[item[1] + 1:]
        seating_chart[item[0]] = row
    return seating_chart


def count_occupied_adjacent_seats(row, column, seating_chart):
    height = len(seating_chart) - 1
    width = len(seating_chart[row]) - 1
    occupied = 0
    if row > 0 and column > 0 and seating_chart[row - 1][column - 1] == '#':
        occupied += 1
    if row > 0 and seating_chart[row - 1][column] == '#':
        occupied += 1
    if row > 0 and column < width and seating_chart[row - 1][column + 1] == '#':
        occupied += 1
    if column > 0 and seating_chart[row][column - 1] == '#':
        occupied += 1
    if column < width and seating_chart[row][column + 1] == '#':
        occupied += 1
    if row < height and column > 0 and seating_chart[row + 1][column - 1] == '#':
        occupied += 1
    if row < height and seating_chart[row + 1][column] == '#':
        occupied += 1
    if row < height and column < width and seating_chart[row + 1][column + 1] == '#':
        occupied += 1
    return occupied


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        test_input1 = ['L#L', '#L#', 'L#L']
        test_input2 = ['#L#', 'L#L', '#L#']
        assert_with_message(2, count_occupied_adjacent_seats(0, 0, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(0, 1, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(0, 2, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(1, 0, test_input1))
        assert_with_message(4, count_occupied_adjacent_seats(1, 1, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(1, 2, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(2, 0, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(2, 1, test_input1))
        assert_with_message(2, count_occupied_adjacent_seats(2, 2, test_input1))
        assert_with_message(1, count_occupied_adjacent_seats(0, 0, test_input2))
        assert_with_message(3, count_occupied_adjacent_seats(0, 1, test_input2))
        assert_with_message(1, count_occupied_adjacent_seats(0, 2, test_input2))
        assert_with_message(3, count_occupied_adjacent_seats(1, 0, test_input2))
        assert_with_message(4, count_occupied_adjacent_seats(1, 1, test_input2))
        assert_with_message(3, count_occupied_adjacent_seats(1, 2, test_input2))
        assert_with_message(1, count_occupied_adjacent_seats(2, 0, test_input2))
        assert_with_message(3, count_occupied_adjacent_seats(2, 1, test_input2))
        assert_with_message(1, count_occupied_adjacent_seats(2, 2, test_input2))
        expected_result1 = ['#L#', 'LLL', '#L#']
        assert_with_message(expected_result1, update_seats(['###', '###', '###']))
        expected_result2 = ['.##', '#.#', '##.']
        assert_with_message(expected_result2, update_seats(['.LL', 'L.L', 'LL.']))
        given_input1 = ['L.LL.LL.LL',
                      'LLLLLLL.LL',
                      'L.L.L..L..',
                      'LLLL.LL.LL',
                      'L.LL.LL.LL',
                      'L.LLLLL.LL',
                      '..L.L.....',
                      'LLLLLLLLLL',
                      'L.LLLLLL.L',
                      'L.LLLLL.LL']
        given_input2 = ['#.##.##.##',
                        '#######.##',
                        '#.#.#..#..',
                        '####.##.##',
                        '#.##.##.##',
                        '#.#####.##',
                        '..#.#.....',
                        '##########',
                        '#.######.#',
                        '#.#####.##']
        assert_with_message(given_input2, update_seats(given_input1))
        given_input3 = ['#.LL.L#.##',
                        '#LLLLLL.L#',
                        'L.L.L..L..',
                        '#LLL.LL.L#',
                        '#.LL.LL.LL',
                        '#.LLLL#.##',
                        '..L.L.....',
                        '#LLLLLLLL#',
                        '#.LLLLLL.L',
                        '#.#LLLL.##']
        assert_with_message(given_input3, update_seats(given_input2))
        given_input4 = ['#.##.L#.##',
                       '#L###LL.L#',
                       'L.#.#..#..',
                       '#L##.##.L#',
                       '#.##.LL.LL',
                       '#.###L#.##',
                       '..#.#.....',
                       '#L######L#',
                       '#.LL###L.L',
                       '#.#L###.##']
        assert_with_message(given_input4, update_seats(given_input3))
        given_input5 = ['#.#L.L#.##', '#LLL#LL.L#', 'L.L.L..#..', '#LLL.##.L#', '#.LL.LL.LL', '#.LL#L#.##',
                        '..L.L.....', '#L#LLLL#L#', '#.LLLLLL.L', '#.#L#L#.##']
        assert_with_message(given_input5, update_seats(given_input4))
        given_input6 = ['#.#L.L#.##', '#LLL#LL.L#', 'L.#.L..#..', '#L##.##.L#', '#.#L.LL.LL', '#.#L#L#.##',
                        '..L.L.....', '#L#L##L#L#', '#.LLLLLL.L', '#.#L#L#.##']
        assert_with_message(given_input6, update_seats(given_input5))
        assert_with_message(37, get_num_occupied_after_updates(given_input1))
        assert_with_message(2418, get_num_occupied_after_updates(get_input(11)))

        run()
