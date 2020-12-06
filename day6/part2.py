import unittest

from aoc_util import get_lines
from aoc_util import assert_with_message


def get_total(lines):
    results = []
    current = []
    for line in lines:
        if len(line) > 0:
            current = current + [line]
        else:
            setcurrent = current[0]
            i = 1
            while i < len(current):
                setcurrent = set(setcurrent).intersection(set(current[i]))
                i = i + 1
            results = results + [len(setcurrent)]
            current = []
    setcurrent = current[0]
    i = 1
    while i < len(current):
        setcurrent = set(setcurrent).intersection(set(current[i]))
        i = i + 1
    results = results + [len(setcurrent)]
    total = 0
    for i in range(len(results)):
        total = total + results[i]
    return total


def part2():
    print(get_total(get_lines('day6.input')))


class TestStringMethods(unittest.TestCase):

    def test_part1(self):
        test_input = ['abc',
                      '',
                      'a',
                      'b',
                      'c',
                      '',
                      'ab',
                      'ac',
                      '',
                      'a',
                      'a',
                      'a',
                      'a',
                      '',
                      'b']
        assert_with_message(6, get_total(test_input))
        part2()
