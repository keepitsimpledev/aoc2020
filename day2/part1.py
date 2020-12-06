import unittest
from collections import Counter

from aoc_util import get_lines
from aoc_util import assert_with_message


# returns [min, max, letter, pass]
def parse_policy_and_pass(policy_and_pass_string):
    minmax_lettercolonpass = policy_and_pass_string.partition(' ')
    min_occurrence = int(minmax_lettercolonpass[0].partition('-')[0])
    max_occurrence = int(minmax_lettercolonpass[0].partition('-')[2])
    letter = minmax_lettercolonpass[2][0]
    password = minmax_lettercolonpass[2].partition(' ')[2]

    return [min_occurrence, max_occurrence, letter, password]


def is_valid(policy_and_pass_string):
    min_max_letter_pass = parse_policy_and_pass(policy_and_pass_string)
    assert_with_message(4, len(min_max_letter_pass))
    counter = Counter(min_max_letter_pass[3])
    count = counter[min_max_letter_pass[2]]
    return min_max_letter_pass[0] <= count <= min_max_letter_pass[1]


def part1():
    entries = get_lines('day2.input')
    num_valid = 0;
    for entry in entries:
        if is_valid(entry):
            num_valid = num_valid + 1
    print('number of valid passes: {}'.format(num_valid))


class TestStringMethods(unittest.TestCase):

    def test_part1(self):
        test1_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        assert_with_message(4, len(parse_policy_and_pass(test1_input[0])))
        assert_with_message(1, parse_policy_and_pass(test1_input[0])[0])
        assert_with_message(3, parse_policy_and_pass(test1_input[0])[1])
        assert_with_message('a', parse_policy_and_pass(test1_input[0])[2])
        assert_with_message('abcde', parse_policy_and_pass(test1_input[0])[3])
        assert is_valid(test1_input[0])
        assert not is_valid(test1_input[1])
        assert is_valid(test1_input[2])
        part1()
