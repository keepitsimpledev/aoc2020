import unittest
import sys

from aoc_util import assert_with_message
from aoc_util import get_input


def is_sum_of_previous(sum, addends):
    for i in range(len(addends)):
        for j in range(i + 1, len(addends)):
            if addends[i] + addends[j] == sum:
                return True
    return False


def find_not_sum(addends, lookback):
    current_index = lookback
    while current_index < len(addends):
        if not is_sum_of_previous(addends[current_index], addends[current_index - lookback: current_index]):
            return addends[current_index]
        current_index += 1
    raise Exception('all sums accounted for')


def find_addends_of_sum(addends, target_sum):
    for i in range(len(addends)):
        current_sum = 0
        low = sys.maxsize
        high = -low
        for j in range(i, len(addends)):
            high = addends[j] if addends[j] > high else high
            low = addends[j] if addends[j] < low else low
            current_sum += addends[j]
            if current_sum == target_sum:
                return low + high
    raise Exception('all sums accounted for')


def input_strings_to_ints(strings_in):
    return list(map(int, strings_in))


def run():
    print()


class TestStringMethods(unittest.TestCase):

    def test_today(self):
        assert_with_message(True, is_sum_of_previous(13, [1, 2, 3, 10, 14, 15]))
        assert_with_message(True, is_sum_of_previous(16, [1, 2, 3, 4, 14, 15]))
        assert_with_message(10, find_not_sum([1, 2, 3, 10, 14, 15], 3))
        assert_with_message(14, find_not_sum([1, 2, 3, 4, 14, 15], 3))
        test_input = input_strings_to_ints(['35', '20', '15', '25', '47', '40', '62', '55', '65', '95', '102', '117',
                                            '150', '182', '127', '219', '299', '277', '309', '576'])
        assert_with_message(127, find_not_sum(test_input, 5))
        day_input_string = get_input(9)
        day_input = input_strings_to_ints(day_input_string[:len(day_input_string) - 1])
        assert_with_message(29221323, find_not_sum(day_input, 25))
        assert_with_message(62, find_addends_of_sum(test_input, find_not_sum(test_input, 5)))
        assert_with_message(4389369, find_addends_of_sum(day_input, find_not_sum(day_input, 25)))
        run()
