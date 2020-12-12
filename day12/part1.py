import unittest
import copy

from aoc_util import assert_with_message
from aoc_util import get_input


def navigate_and_get_hattie_dist(instructions):
    ship_and_waypoint_location = [[0, 0], [10, 1]]
    for instruction in instructions:
        ship_and_waypoint_location = process_instruction(ship_and_waypoint_location, instruction)
    return abs(ship_and_waypoint_location[0][0]) + abs(ship_and_waypoint_location[0][1])


def process_instruction(locations_and_heading, instruction):
    value = int(instruction[1:])
    ship_location = locations_and_heading[0]
    waypoint_location = locations_and_heading[1]
    if instruction[0] == 'N':
        waypoint_location[1] += value
    elif instruction[0] == 'E':
        waypoint_location[0] += value
    elif instruction[0] == 'S':
        waypoint_location[1] -= value
    elif instruction[0] == 'W':
        waypoint_location[0] -= value
    elif instruction[0] == 'R':
        turns = value / 90 % 4
        new_location = copy.deepcopy(waypoint_location)
        if turns == 1:
            new_location[0] = waypoint_location[1]
            new_location[1] = -waypoint_location[0]
        if turns == 2:
            new_location[0] = -waypoint_location[0]
            new_location[1] = -waypoint_location[1]
        if turns == 3:
            new_location[0] = -waypoint_location[1]
            new_location[1] = waypoint_location[0]
        waypoint_location = new_location
    elif instruction[0] == 'L':
        turns = value / 90 % 4
        new_location = copy.deepcopy(waypoint_location)
        if turns == 1:
            new_location[0] = -waypoint_location[1]
            new_location[1] = waypoint_location[0]
        if turns == 2:
            new_location[0] = -waypoint_location[0]
            new_location[1] = -waypoint_location[1]
        if turns == 3:
            new_location[0] = waypoint_location[1]
            new_location[1] = -waypoint_location[0]
        waypoint_location = new_location
    elif instruction[0] == 'F':
        for i in range(value):
            ship_location[0] += waypoint_location[0]
            ship_location[1] += waypoint_location[1]
    else:
        raise 'unexpected instruction: {}'.format(instruction)
    return [ship_location, waypoint_location]


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        test_ship = [0, 0]
        test_waypoint = [10, 1]
        test_start = [test_ship, test_waypoint]
        assert_with_message([test_ship, [10, 2]], process_instruction(copy.deepcopy(test_start), 'N1'))
        assert_with_message([test_ship, [12, 1]], process_instruction(copy.deepcopy(test_start), 'E2'))
        assert_with_message([test_ship, [10, -2]], process_instruction(copy.deepcopy(test_start), 'S3'))
        assert_with_message([test_ship, [6, 1]], process_instruction(copy.deepcopy(test_start), 'W4'))
        assert_with_message([[50, 5], test_waypoint], process_instruction(copy.deepcopy(test_start), 'F5'))
        assert_with_message([test_ship, [1, -10]], process_instruction(copy.deepcopy(test_start), 'R90'))
        assert_with_message([test_ship, [-10, -1]], process_instruction(copy.deepcopy(test_start), 'L180'))
        assert_with_message([test_ship, [-1, 10]], process_instruction(copy.deepcopy(test_start), 'R270'))
        assert_with_message([test_ship, [10, 1]], process_instruction(copy.deepcopy(test_start), 'L360'))
        given_input1 = ['F10', 'N3', 'F7', 'R90', 'F11']
        assert_with_message(286, navigate_and_get_hattie_dist(given_input1))
        assert_with_message(52866, navigate_and_get_hattie_dist(get_input(12)))
        run()
