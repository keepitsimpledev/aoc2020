import unittest

from aoc_util import get_lines
from aoc_util import assert_with_message


def count_trees(map_lines, move):
    num_trees = 0
    current_location = 0
    if map_lines.pop(0)[0] == '#':
        num_trees = num_trees + 1
    for line in map_lines:
        current_location = (current_location + move) % len(line)
        if line[current_location] == '#':
            num_trees = num_trees + 1
    return num_trees


def part1():
    print(count_trees(get_lines('day3.input'), 3))


class TestStringMethods(unittest.TestCase):

    def test_part1(self):
        test_input = ['..##.......',
                      '#...#...#..',
                      '.#....#..#.',
                      '..#.#...#.#',
                      '.#...##..#.',
                      '..#.##.....',
                      '.#.#.#....#',
                      '.#........#',
                      '#.##...#...',
                      '#...##....#',
                      '.#..#...#.#']
        assert_with_message(count_trees(test_input, 3) == 7, 7, count_trees(test_input, 3))
        part1()
