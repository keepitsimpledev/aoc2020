import unittest

from aoc_util import assert_with_message
from aoc_util import get_input


def get_final_acc(commands_input):
    commands_table = []
    for command in commands_input:
        if len(command) > 0:
            commands_table += [[command.split(' ')[0], command.split(' ')[1], False]] #command, argument, has executed
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
    return accumulator


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
        assert_with_message(5, get_final_acc(test_input))
        assert_with_message(1818, get_final_acc(get_input(8)))
        run()
