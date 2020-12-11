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
            if seating_chart[i][j] != '#' and count_occupied_seats_in_all_directions(i, j, seating_chart) == 0:
                to_update += [[i, j, '#']]
            elif seating_chart[i][j] == '#' and count_occupied_seats_in_all_directions(i, j, seating_chart) >= 5:
                to_update += [[i, j, 'L']]
    for item in to_update:
        row = seating_chart[item[0]]
        row = row[:item[1]] + item[2] + row[item[1] + 1:]
        seating_chart[item[0]] = row
    return seating_chart


def count_occupied_seats_in_all_directions(row, column, seating_chart):
    _ROW = 'row'
    _COLUMN = 'column'
    height = len(seating_chart) - 1
    width = len(seating_chart[row]) - 1
    occupied = 0

    current = {'row': row, 'column': column}
    while current[_ROW] > 0 and current[_COLUMN] > 0:
        current[_ROW] -= 1
        current[_COLUMN] -= 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_ROW] > 0:
        current[_ROW] -= 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_ROW] > 0 and current[_COLUMN] < width:
        current[_ROW] -= 1
        current[_COLUMN] += 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_COLUMN] > 0:
        current[_COLUMN] -= 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_COLUMN] < width:
        current[_COLUMN] += 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_ROW] < height and current[_COLUMN] > 0:
        current[_ROW] += 1
        current[_COLUMN] -= 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_ROW] < height:
        current[_ROW] += 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    current[_ROW] = row
    current[_COLUMN] = column
    while current[_ROW] < height and current[_COLUMN] < width:
        current[_ROW] += 1
        current[_COLUMN] += 1
        if seating_chart[current[_ROW]][current[_COLUMN]] == 'L':
            break
        if seating_chart[current[_ROW]][current[_COLUMN]] == '#':
            occupied += 1
            break

    return occupied


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        test_input1 = ['L#L',
                       '#L#',
                       'L#L']
        test_input2 = ['#L#',
                       'L#L',
                       '#L#']
        assert_with_message(2, count_occupied_seats_in_all_directions(0, 0, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(0, 1, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(0, 2, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(1, 0, test_input1))
        assert_with_message(4, count_occupied_seats_in_all_directions(1, 1, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(1, 2, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(2, 0, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(2, 1, test_input1))
        assert_with_message(2, count_occupied_seats_in_all_directions(2, 2, test_input1))
        assert_with_message(1, count_occupied_seats_in_all_directions(0, 0, test_input2))
        assert_with_message(3, count_occupied_seats_in_all_directions(0, 1, test_input2))
        assert_with_message(1, count_occupied_seats_in_all_directions(0, 2, test_input2))
        assert_with_message(3, count_occupied_seats_in_all_directions(1, 0, test_input2))
        assert_with_message(4, count_occupied_seats_in_all_directions(1, 1, test_input2))
        assert_with_message(3, count_occupied_seats_in_all_directions(1, 2, test_input2))
        assert_with_message(1, count_occupied_seats_in_all_directions(2, 0, test_input2))
        assert_with_message(3, count_occupied_seats_in_all_directions(2, 1, test_input2))
        assert_with_message(1, count_occupied_seats_in_all_directions(2, 2, test_input2))
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
        given_input2 = ['#.##.##.##', '#######.##', '#.#.#..#..', '####.##.##', '#.##.##.##', '#.#####.##',
                        '..#.#.....', '##########', '#.######.#', '#.#####.##']
        assert_with_message(given_input2, update_seats(given_input1))
        given_input3 = ['#.LL.LL.L#', '#LLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL',
                        '..L.L.....', 'LLLLLLLLL#', '#.LLLLLL.L', '#.LLLLL.L#']
        assert_with_message(given_input3, update_seats(given_input2))
        given_input4 = ['#.L#.##.L#', '#L#####.LL', 'L.#.#..#..', '##L#.##.##', '#.##.#L.##', '#.#####.#L',
                        '..#.#.....', 'LLL####LL#', '#.L#####.L', '#.L####.L#']
        assert_with_message(given_input4, update_seats(given_input3))
        given_input5 = ['#.L#.L#.L#', '#LLLLLL.LL', 'L.L.L..#..', '##LL.LL.L#', 'L.LL.LL.L#', '#.LLLLL.LL',
                        '..L.L.....', 'LLLLLLLLL#', '#.LLLLL#.L', '#.L#LL#.L#']
        assert_with_message(given_input5, update_seats(given_input4))
        given_input6 = ['#.L#.L#.L#', '#LLLLLL.LL', 'L.L.L..#..', '##L#.#L.L#', 'L.L#.#L.L#', '#.L####.LL',
                        '..#.#.....', 'LLL###LLL#', '#.LLLLL#.L', '#.L#LL#.L#']
        assert_with_message(given_input6, update_seats(given_input5))
        given_input7 = ['#.L#.L#.L#', '#LLLLLL.LL', 'L.L.L..#..', '##L#.#L.L#', 'L.L#.LL.L#', '#.LLLL#.LL',
                        '..#.L.....', 'LLL###LLL#', '#.LLLLL#.L', '#.L#LL#.L#']
        assert_with_message(given_input7, update_seats(given_input6))
        assert_with_message(26, get_num_occupied_after_updates(given_input1))
        assert_with_message(2144, get_num_occupied_after_updates(get_input(11)))

        run()
