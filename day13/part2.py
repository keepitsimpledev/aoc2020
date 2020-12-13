import unittest

from aoc_util import assert_with_message
from aoc_util import get_input


def process_input(time_and_schedules):
    schedules_str = time_and_schedules[1].split(',')
    schedules = []
    for i in range(len(schedules_str)):
        if schedules_str[i] != 'x':
            schedules += [[int(schedules_str[i]), i]]
    return schedules


def find_consecutive_schedule(bus_and_interval):
    values = []
    for bus in bus_and_interval:
        values += [bus[0]]
    current_index = 0
    path_found = False
    while not path_found:
        curr_val = values[current_index]
        next_val = bus_and_interval[current_index + 1][0]
        next_val = int(curr_val / next_val) * next_val + next_val
        values[current_index + 1] = next_val
        gap = bus_and_interval[current_index + 1][1] - bus_and_interval[current_index][1]
        if curr_val == next_val - gap:
            if current_index == len(bus_and_interval) - 2:
                path_found = True
            else:
                current_index += 1
        else:
            values[0] += bus_and_interval[0][0]
            current_index = 0
    return values[0]


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        given_input1 = ['939', '7,13,x,x,59,x,31,19']
        processed_given_input1 = process_input(given_input1)
        assert_with_message([[7, 0], [13, 1], [59, 4], [31, 6], [19, 7]], processed_given_input1)

        assert_with_message(2, find_consecutive_schedule([[2, 0], [3, 1]]))

        assert_with_message(11, find_consecutive_schedule([[11, 0], [4, 1]]))
        assert_with_message(15, find_consecutive_schedule([[5, 0], [4, 1]]))
        assert_with_message(8, find_consecutive_schedule([[2, 0], [5, 2]]))
        assert_with_message(14, find_consecutive_schedule([[7, 0], [5, 1], [4, 2]]))
        assert_with_message(1, find_consecutive_schedule([[1, 0], [2, 1], [3, 2]]))
        assert_with_message(12, find_consecutive_schedule([[2, 0], [5, 3], [6, 6]]))
        assert_with_message(20, find_consecutive_schedule([[5, 0], [7, 1], [11, 2]]))
        assert_with_message(2, find_consecutive_schedule([[2, 0], [2, 2], [2, 4]]))

        test_input1 = process_input(given_input1)
        assert_with_message(1068781, find_consecutive_schedule(test_input1))
        test_input2 = process_input(['', '17,x,13,19'])
        assert_with_message(3417, find_consecutive_schedule(test_input2))
        test_input3 = process_input(['', '67,7,59,61'])
        assert_with_message(754018, find_consecutive_schedule(test_input3))
        test_input4 = process_input(['', '67,x,7,59,61'])
        assert_with_message(779210, find_consecutive_schedule(test_input4))
        test_input5 = process_input(['', '67,7,x,59,61'])
        assert_with_message(1261476, find_consecutive_schedule(test_input5))
        test_input5 = process_input(['', '1789,37,47,1889'])
        assert_with_message(1202161486, find_consecutive_schedule(test_input5))

        day_input = process_input(get_input(13))
        # assert_with_message(1202161486, find_consecutive_schedule(day_input))

        run()
