import unittest
import sys
from math import ceil

from aoc_util import assert_with_message
from aoc_util import get_input


def process_input(time_and_schedules):
    time = time_and_schedules[0]
    schedules_str = time_and_schedules[1].split(',')
    schedules = []
    for item in schedules_str:
        if item != 'x':
            schedules += [int(item)]
    return [int(time), schedules]


def get_soonest_bus_times_wait(time_and_schedules):
    processed_time_and_schedules_input = process_input(time_and_schedules)
    time = processed_time_and_schedules_input[0]
    schedule = processed_time_and_schedules_input[1]
    soonest_bus = -1
    lowest_wait = sys.maxsize
    for bus in schedule:
        time_until_bus = ceil(time / bus) * bus - time
        if time_until_bus < lowest_wait:
            lowest_wait = time_until_bus
            soonest_bus = bus
    return soonest_bus * lowest_wait


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        given_input1 = ['939', '7,13,x,x,59,x,31,19']
        assert_with_message([939, [7, 13, 59, 31, 19]], process_input(given_input1))
        assert_with_message(295, get_soonest_bus_times_wait(given_input1))
        assert_with_message(104, get_soonest_bus_times_wait(get_input(13)))
        run()
