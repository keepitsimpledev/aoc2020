import unittest

from aoc_util import assert_with_message
from aoc_util import get_input
from aoc_util import input_strings_to_ints


def get_num_1_and_3_joltage_gaps(adapters):
    gaps = {1: 0, 2: 0, 3: 1}
    adapters.sort()
    gaps[adapters[0]] += 1
    for i in range(len(adapters) - 1):
        gaps[adapters[i + 1] - adapters[i]] += 1
    return [gaps[1], gaps[3]]


def get_num_1_and_3_joltage_gap_product(adapters):
    gaps = get_num_1_and_3_joltage_gaps(adapters)
    return gaps[0] * gaps[1]


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        test_input1 = input_strings_to_ints(['16', '10', '15', '5', '1', '11', '7', '19', '6', '12', '4'])
        assert_with_message([7, 5], get_num_1_and_3_joltage_gaps(test_input1))
        test_input2 = input_strings_to_ints(['28', '33', '18', '42', '31', '14', '46', '20', '48', '47', '24', '23',
                                             '49', '45', '19', '38', '39', '11', '1', '32', '25', '35', '8', '17', '7',
                                             '9', '4', '2', '34', '10', '3'])
        assert_with_message([22, 10], get_num_1_and_3_joltage_gaps(test_input2))
        day_input = get_input(10)
        if day_input[len(day_input) - 1] == '':
            day_input = day_input[:len(day_input) - 1]
        day_input = input_strings_to_ints(day_input)
        assert_with_message([72, 31], get_num_1_and_3_joltage_gaps(day_input))
        assert_with_message(2232, get_num_1_and_3_joltage_gap_product(day_input))
        run()
