import unittest

from aoc_util import assert_with_message
from aoc_util import get_input


def get_final_acc(commands_input):
    commands_table = []
    for command in commands_input:
        if len(command) > 0:
            commands_table += [[command.split(' ')[0], command.split(' ')[1], False]] #command, argument, has executed
    last_flipped_index = 0
    flip_search_index = 0
    while flip_search_index < len(commands_table):
        flipped = False
        while not flipped:
            if flip_search_index == len(commands_table):
                raise Exception('solution not found. runtime should not reach here.')
            if commands_table[flip_search_index][0] in ('nop', 'jmp'):
                flip(commands_table[flip_search_index])
                flipped = True
            flip_search_index += 1
        accumulator = 0
        current_command_index = 0
        while not commands_table[current_command_index][2]:
            commands_table[current_command_index][2] = True
            operation = commands_table[current_command_index][0]
            argument = int(commands_table[current_command_index][1])
            if operation == 'acc':
                accumulator += argument
                current_command_index += 1
            elif operation == 'jmp':
                current_command_index += argument
            elif operation == 'nop':
                current_command_index += 1
            else:
                raise Exception('invalid operation: {}'.format(operation))
            if current_command_index == len(commands_table):
                return accumulator
        reset(commands_table)
        flip(commands_table[flip_search_index - 1])
    raise Exception('solution not found. runtime should not reach here.')


def flip(command):
    if command[0] == 'nop':
        command[0] = 'jmp'
    elif command[0] == 'jmp':
        command[0] = 'nop'
    else:
        raise Exception('expected nop or jmp but got {}'.format(command[0]))


def reset(commands_table):
    for i in range(len(commands_table)):
        commands_table[i][2] = False


def run():
    print()


class TestStringMethods(unittest.TestCase):

    def test_today(self):
        test_input = ['nop +0',
                      'acc +1',
                      'jmp +4',
                      'acc +3',
                      'jmp -3',
                      'acc -99',
                      'acc +1',
                      'jmp -4',
                      'acc +6']
        assert_with_message(8, get_final_acc(test_input))
        assert_with_message(631, get_final_acc(get_input(8)))
        run()
