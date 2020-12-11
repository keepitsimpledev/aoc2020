import unittest

from aoc_util import assert_with_message
from aoc_util import get_input
from aoc_util import input_strings_to_ints


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
        run()
