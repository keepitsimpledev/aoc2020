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


def find_consecutive_schedule(busses_and_intervals):
    current_values = []
    for item in busses_and_intervals:
        current_values += [item[0]]
    highest_and_second = find_highest_and_penultimate(busses_and_intervals)
    for i in range(len(busses_and_intervals)):
        if busses_and_intervals[i][0] == highest_and_second[0][0]:
            fulcrum_index = i
            break
    current_values[fulcrum_index] = get_consecutive_schedule_with_minimum(highest_and_second[0],
                                                                          highest_and_second[1], 0)
    solution_found = False
    while not solution_found:
        current_solution_looks_good = True
        left_index = fulcrum_index
        while left_index > 0:
            current_value = current_values[left_index]
            left_bus = busses_and_intervals[left_index - 1][0]
            left_gap = busses_and_intervals[left_index][1] - busses_and_intervals[left_index - 1][1]
            if (current_value - left_gap) % left_bus == 0:
                current_values[left_index - 1] = current_value - left_gap
                left_index -= 1
            else:
                current_solution_looks_good = False
                break
        if current_solution_looks_good:
            right_index = fulcrum_index
            while right_index < len(busses_and_intervals) - 1:
                current_value = current_values[right_index]
                right_bus = busses_and_intervals[right_index + 1][0]
                right_gap = busses_and_intervals[right_index + 1][1] - busses_and_intervals[right_index][1]
                if (current_value + right_gap) % right_bus == 0:
                    current_values[right_index + 1] = current_value + right_gap
                    right_index += 1
                else:
                    current_solution_looks_good = False
                    break
        if current_solution_looks_good:
            return current_values[0]
        else:
            current_values[fulcrum_index] = get_consecutive_schedule_with_minimum(
                highest_and_second[0], highest_and_second[1], current_values[fulcrum_index] + 1)


def find_highest_and_penultimate(bus_and_interval):
    highest = [-1, -1]
    second_highest = [-1, -1]
    for item in bus_and_interval:
        if item[0] > highest[0]:
            second_highest = highest
            highest = item
        elif second_highest[0] < item[0] <= highest[0]:
            second_highest = item
    return [highest, second_highest]


def get_consecutive_schedule_with_minimum(bus1, bus2, minimum):
    bus1_time = int(minimum / bus1[0]) * bus1[0]
    if bus1_time < minimum or bus1_time == 0:
        bus1_time += bus1[0]
    bus2_time = int(minimum / bus2[0]) * bus2[0]
    if bus2_time < minimum or bus2_time == 0:
        bus2_time += bus2[0]
    gap = bus2[1] - bus1[1]
    while bus1_time != bus2_time - gap:
        if bus2_time - bus1_time >= gap:
            bus1_time += bus1[0]
        else:
            bus2_time += bus2[0]
    return bus1_time


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        assert_with_message([[59, 1], [4, 2]], find_highest_and_penultimate([[2, 0], [59, 1], [4, 2], [3, 3]]))
        assert_with_message([[11, 2], [4, 1]], find_highest_and_penultimate([[2, 0], [4, 1], [11, 2], [3, 3]]))
        assert_with_message([[100, 0], [33, 3]], find_highest_and_penultimate([[100, 0], [4, 1], [11, 2], [33, 3]]))
        assert_with_message([[100, 3], [33, 0]], find_highest_and_penultimate([[33, 0], [4, 1], [11, 2], [100, 3]]))
        assert_with_message([[2, 0], [2, 2]], find_highest_and_penultimate([[2, 0], [2, 2], [2, 4]]))
        assert_with_message(11, get_consecutive_schedule_with_minimum([11, 0], [4, 1], 10))
        assert_with_message(15, get_consecutive_schedule_with_minimum([5, 0], [4, 1], 10))
        assert_with_message(8, get_consecutive_schedule_with_minimum([2, 0], [5, 2], 0))
        assert_with_message(18, get_consecutive_schedule_with_minimum([2, 0], [5, 2], 10))

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
        assert_with_message(1202161486, find_consecutive_schedule(day_input))

        run()
