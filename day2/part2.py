import unittest

from aoc_util import get_lines
from aoc_util import assert_with_message


# returns [min, max, letter, pass]
def parse_policy_and_pass(policy_and_pass_string):
    positions_lettercolonpass = policy_and_pass_string.partition(' ')
    position1 = int(positions_lettercolonpass[0].partition('-')[0]) - 1
    position2 = int(positions_lettercolonpass[0].partition('-')[2]) - 1
    letter = positions_lettercolonpass[2][0]
    password = positions_lettercolonpass[2].partition(' ')[2]

    return [position1, position2, letter, password]


def is_valid(policy_and_pass_string):
    pos1_pos2_letter_pass = parse_policy_and_pass(policy_and_pass_string)
    assert_with_message(len(pos1_pos2_letter_pass) == 4, 4, len(pos1_pos2_letter_pass))
    letter = pos1_pos2_letter_pass[2]
    password = pos1_pos2_letter_pass[3]
    found_at_pos1 = password[pos1_pos2_letter_pass[0]] == letter
    found_at_pos2 = password[pos1_pos2_letter_pass[1]] == letter
    return found_at_pos1 ^ found_at_pos2


def part1():
    entries = get_lines('day2.input')
    num_valid = 0;
    for entry in entries:
        if (is_valid(entry)):
            num_valid = num_valid + 1
    print('number of valid passes: {}'.format(num_valid))


class TestStringMethods(unittest.TestCase):

    def test_part2(self):
        test1_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        assert_with_message(len(parse_policy_and_pass(test1_input[0])) == 4, 4,
                            len(parse_policy_and_pass(test1_input[0])))
        assert_with_message(parse_policy_and_pass(test1_input[0])[0] == 0, 0, parse_policy_and_pass(test1_input[0])[0])
        assert_with_message(parse_policy_and_pass(test1_input[0])[1] == 2, 2, parse_policy_and_pass(test1_input[0])[1])
        assert_with_message(parse_policy_and_pass(test1_input[0])[2] == 'a', 'a',
                            parse_policy_and_pass(test1_input[0])[2])
        assert_with_message(parse_policy_and_pass(test1_input[0])[3] == 'abcde', 'abcde',
                            parse_policy_and_pass(test1_input[0])[3])
        assert is_valid(test1_input[0])
        assert not is_valid(test1_input[1])
        assert not is_valid(test1_input[2])
        part1()
