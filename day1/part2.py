import unittest

from aoc_util import get_lines


def get_addends_of_2020(numbers):
    first_addend = 0
    second_addend = 1
    third_addend = 2
    try:
        while numbers[first_addend] + numbers[second_addend] + numbers[third_addend] != 2020:
            if third_addend >= len(numbers):
                raise Exception('something went wrong. index is larger than list size.')
            elif third_addend == len(numbers) - 1 and second_addend == len(numbers) - 2:
                first_addend = first_addend + 1
                second_addend = first_addend + 1
                third_addend = first_addend + 2
            elif third_addend == len(numbers) - 1:
                second_addend = second_addend + 1
                third_addend = second_addend + 1
            else:
                third_addend = third_addend + 1
        print('first_addend {} second_addend {} third_addend {}'.format(first_addend, second_addend, third_addend))
        return [numbers[first_addend], numbers[second_addend], numbers[third_addend]]
    except IndexError:
        print('first_addend {} second_addend {} third_addend {}'.format(first_addend, second_addend, third_addend))


def part2():
    entries = get_lines('day1.input')
    addends_of_2020 = get_addends_of_2020(entries)
    print("{} + {} + {} = {}".format(addends_of_2020[0], addends_of_2020[1], addends_of_2020[2],
                                     addends_of_2020[0] + addends_of_2020[1] + addends_of_2020[2]))
    print("{} + {} + {} = {}".format(addends_of_2020[0], addends_of_2020[1], addends_of_2020[2],
                                     addends_of_2020[0] * addends_of_2020[1] * addends_of_2020[2]))


class TestStringMethods(unittest.TestCase):

    def test_part2(self):
        test1_input = [1234, 20, 4312, 980, 1020]
        test1_output = get_addends_of_2020(test1_input)
        assert test1_output[0] == 20 and test1_output[1] == 980 and test1_output[2] == 1020
        part2()
