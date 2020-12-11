import unittest
from collections import deque

from aoc_util import assert_with_message
from aoc_util import get_input
from aoc_util import input_strings_to_ints


# @Precondition: adapters is sorted
def get_num_configs_recursively(adapters):
    configs = 0
    if len(adapters) == 1:
        configs += 1
    if len(adapters) >= 4 and adapters[3] - adapters[0] == 3:
        configs += get_num_configs_recursively(adapters[3:])
    if len(adapters) >= 3 and adapters[2] - adapters[0] <= 3:
        configs += get_num_configs_recursively(adapters[2:])
    if len(adapters) >= 2:
        configs += get_num_configs_recursively(adapters[1:])
    return configs


def get_num_configs(adapters):
    adapters.sort()
    configs = deque([])
    adapter_index = 0
    use_adapter(adapter_index, [adapters[adapter_index], 1], adapters, configs)
    while configs[0][0] < adapters[-1]:
        next_adapter = configs.popleft()
        adapter_index += 1
        use_adapter(adapter_index, next_adapter, adapters, configs)
    return configs[0][1]


def use_adapter(index, adapter, adapters, configs: deque):
    if len(adapters) > index + 3 and adapters[index + 3] - adapters[index] <= 3:
        insert_config([adapters[index + 3], adapter[1]], configs)
    if len(adapters) > index + 2 and adapters[index + 2] - adapters[index] <= 3:
        insert_config([adapters[index + 2], adapter[1]], configs)
    if len(adapters) > index + 1 and adapters[index + 1] - adapters[index] <= 3:
        insert_config([adapters[index + 1], adapter[1]], configs)
    return index


def insert_config(adapter, configs: deque):
    for i in range(len(configs)):
        if configs[i][0] == adapter[0]:
            configs[i][1] += adapter[1]
            return
        elif configs[i][0] > adapter[0]:
            configs.insert(i, adapter)
            return
    configs.append(adapter)


def run():
    print()


class TestAoC(unittest.TestCase):

    def test_part(self):
        test_input1 = input_strings_to_ints(['16', '10', '15', '5', '1', '11', '7', '19', '6', '12', '4'])
        test_input2 = input_strings_to_ints(['28', '33', '18', '42', '31', '14', '46', '20', '48', '47', '24', '23',
                                             '49', '45', '19', '38', '39', '11', '1', '32', '25', '35', '8', '17', '7',
                                             '9', '4', '2', '34', '10', '3'])
        day_input = get_input(10)
        if day_input[len(day_input) - 1] == '':
            day_input = day_input[:len(day_input) - 1]
        day_input = input_strings_to_ints(day_input)
        test_input1.sort()
        assert_with_message(8, get_num_configs_recursively([0] + test_input1))
        test_input2.sort()
        assert_with_message(19208, get_num_configs_recursively([0] + test_input2))

        assert_with_message(8, get_num_configs([0] + test_input1))
        assert_with_message(19208, get_num_configs([0] + test_input2))
        assert_with_message(173625106649344, get_num_configs([0] + day_input))
        run()
