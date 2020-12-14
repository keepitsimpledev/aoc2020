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
    busses_and_intervals = sorted(busses_and_intervals, reverse=True, key=lambda tup: tup[0])
    solution = []
    for i in range(len(busses_and_intervals)):
        solution += [busses_and_intervals[i][0]]
        if busses_and_intervals[i][1] == 0:
            solution_index = i

    solution_found = False
    while not solution_found:
        current_solution_is_good = True
        for i in range(len(busses_and_intervals) - 1):
            gap_forward = busses_and_intervals[i + 1][1] - busses_and_intervals[i][1]
            schedule = get_consecutive_schedule_with_minimum(busses_and_intervals[i],
                                                             busses_and_intervals[i + 1],
                                                             [solution[i], solution[i] + gap_forward])
            solution[i] = schedule[0]
            solution[i + 1] = schedule[1]
            if i > 0:
                gap_backward = busses_and_intervals[i][1] - busses_and_intervals[i - 1][1]
                if solution[i] - gap_backward != solution[i - 1]:
                    current_solution_is_good = False
                    break
        if not current_solution_is_good:
            solution[0] += busses_and_intervals[0][0]
        else:
            solution_found = True
    return solution[solution_index]


def get_consecutive_schedule_with_minimum(bus1, bus2, minima):
    bus1_time = int(minima[0] / bus1[0]) * bus1[0]
    if bus1_time < minima[0] or bus1_time == 0:
        bus1_time += bus1[0]
    bus2_time = int(minima[1] / bus2[0]) * bus2[0]
    if bus2_time < minima[1] or bus2_time == 0:
        bus2_time += bus2[0]
    gap = bus2[1] - bus1[1]
    while bus1_time != bus2_time - gap:
        if bus2_time - bus1_time >= gap:
            bus1_time += bus1[0]
        else:
            bus2_time += bus2[0]
    return [bus1_time, bus2_time]


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        assert_with_message([11, 12], get_consecutive_schedule_with_minimum([11, 0], [4, 1], [10, 10]))
        assert_with_message([15, 16], get_consecutive_schedule_with_minimum([5, 0], [4, 1], [10, 10]))
        assert_with_message([8, 10], get_consecutive_schedule_with_minimum([2, 0], [5, 2], [0, 0]))
        assert_with_message([18, 20], get_consecutive_schedule_with_minimum([2, 0], [5, 2], [10, 10]))

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
