import unittest
import copy
import sys
from math import ceil

from aoc_util import assert_with_message
from aoc_util import get_input
from aoc_util import input_strings_to_ints


def process_input(time_and_schedules):
    schedules_str = time_and_schedules[1].split(',')
    schedules = []
    for i in range(len(schedules_str)):
        if schedules_str[i] != 'x':
            schedules += [[int(schedules_str[i]), i]]
    return schedules


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
    return [bus1_time, bus2_time]


def get_current_and_next_schedule(bus_index, schedules, minimum):
    if bus_index == len(schedules) - 2:
        return get_consecutive_schedule_with_minimum(schedules[bus_index], schedules[bus_index + 1], minimum)
    else:
        bus_times = [minimum, minimum]
        gap_12 = schedules[bus_index + 1][1] - schedules[bus_index][1]

        while bus_times[0] != bus_times[1] - gap_12:
            bus_times = get_consecutive_schedule_with_minimum(schedules[bus_index], schedules[bus_index + 1], minimum)
            next_times =\
                get_current_and_next_schedule(bus_index + 1, schedules, bus_times[1])
            bus_times[1] = next_times[0]
            minimum += schedules[bus_index][0]
        return bus_times


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        given_input1 = ['939', '7,13,x,x,59,x,31,19']
        processed_given_input1 = process_input(given_input1)
        assert_with_message([[7, 0], [13, 1], [59, 4], [31, 6], [19, 7]], processed_given_input1)
        assert_with_message([11, 12], get_consecutive_schedule_with_minimum([11, 0], [4, 1], 10))
        assert_with_message([15, 16], get_consecutive_schedule_with_minimum([5, 0], [4, 1], 10))
        assert_with_message([8, 10], get_consecutive_schedule_with_minimum([2, 0], [5, 2], 0))
        assert_with_message([18, 20], get_consecutive_schedule_with_minimum([2, 0], [5, 2], 10))
        assert_with_message([14, 15], get_current_and_next_schedule(0, [[7, 0], [5, 1], [4, 2]], 0))
        assert_with_message([1, 2], get_current_and_next_schedule(0, [[1, 0], [2, 1], [3, 2]], 0))
        assert_with_message([7, 8], get_current_and_next_schedule(0, [[1, 0], [2, 1], [3, 2]], 2))
        assert_with_message([12, 15], get_current_and_next_schedule(0, [[2, 0], [5, 3], [6, 6]], 2))
        assert_with_message([20, 21], get_current_and_next_schedule(0, [[5, 0], [7, 1], [11, 2]], 0))
        assert_with_message([2, 4], get_current_and_next_schedule(0, [[2, 0], [2, 2], [2, 4]], 0))
        assert_with_message([4, 6], get_current_and_next_schedule(0, [[2, 0], [2, 2], [2, 4]], 4))
        assert_with_message([4, 6], get_current_and_next_schedule(0, [[2, 0], [2, 2], [2, 6]], 3))
        assert_with_message([405, 406], get_current_and_next_schedule(0, [[5, 0], [7, 1], [11, 2]], 25))
        # assert_with_message(1068781, get_current_and_next_schedule(0, processed_given_input1, 0))
        run()
