import unittest

from aoc_util import get_lines


def get_addends_of_2020(numbers):
    anchor_index = 0
    current_index = 1
    try:
        while numbers[anchor_index] + numbers[current_index] != 2020:
            if current_index >= len(numbers):
                raise Exception('something went wrong. index is larger than list size.')
            elif current_index == len(numbers) - 1:
                anchor_index = anchor_index + 1
                current_index = anchor_index + 1
            else:
                current_index = current_index + 1
        print('current {} anchor {}'.format(current_index, anchor_index))
        return [numbers[anchor_index], numbers[current_index]]
    except IndexError:
        print('current {} anchor {}'.format(current_index, anchor_index))


def part1():
    entries = get_lines('day1.input')
    for i in range(len(entries)):
        entries[i] = int(entries[i])
    addends_of_2020 = get_addends_of_2020(entries)
    print("{} + {} = {}".format(addends_of_2020[0], addends_of_2020[1],
                                addends_of_2020[0] + addends_of_2020[1]))
    print("{} x {} = {}".format(addends_of_2020[0], addends_of_2020[1],
                                addends_of_2020[0] * addends_of_2020[1]))


class TestStringMethods(unittest.TestCase):

    def test_part1(self):
        test1_input = [1234, 4312, 1000, 1020]
        test1_output = get_addends_of_2020(test1_input)
        assert test1_output[0] == 1000 and test1_output[1] == 1020
        part1()
