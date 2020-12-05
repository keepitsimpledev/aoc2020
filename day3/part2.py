import unittest

from aoc_util import get_lines
from aoc_util import assert_with_message


def count_trees(map_lines, move_right, move_down=1):
    map_lines = map_lines.copy()
    num_trees = 0
    current_location = 0
    if map_lines[0][0] == '#':
        num_trees = num_trees + 1
    y = move_down
    while y < len(map_lines):
        line = map_lines[y]
        current_location = (current_location + move_right) % len(line)
        if line[current_location] == '#':
            num_trees = num_trees + 1
        y = y + move_down
    return num_trees


def combine_paths(map_lines):
    one_one = count_trees(map_lines, 1)
    three_one = count_trees(map_lines, 3)
    five_one = count_trees(map_lines, 5)
    seven_one = count_trees(map_lines, 7)
    one_two = count_trees(map_lines, 1, 2)
    return one_one * three_one * five_one * seven_one * one_two


def part2():
    map_lines = get_lines('day3.input')
    print('result: {}'.format(combine_paths(map_lines)))


class TestStringMethods(unittest.TestCase):

    def test_part2(self):
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
        assert_with_message(7, count_trees(test_input, 3))
        assert_with_message(336, combine_paths(test_input))
        map_lines = get_lines('day3.input')
        assert_with_message(211, count_trees(map_lines, 3))
        part2()
