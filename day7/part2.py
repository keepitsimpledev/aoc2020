import unittest

from aoc_util import assert_with_message
from aoc_util import get_input


def pre_process_rule(rule: str):
    return rule.replace('bags', 'bag').replace('.', '').replace(',', '')


def get_containing_bag(rule: str):
    rule = pre_process_rule(rule)
    return rule.partition('bag')[0].strip()


def get_contained_bags(rule: str):
    rule = pre_process_rule(rule)
    contained_bags_string = rule.partition('contain')[2]
    contained_bags_list = contained_bags_string.split('bag')
    contained_bags_and_count = None
    for entry in contained_bags_list:
        if entry == '':
            break
        entry = entry.strip()
        partitioned_entry = entry.partition(' ')
        if partitioned_entry[0] == 'no':
            break
        contained_bag_and_count = {partitioned_entry[2]: int(entry.partition(' ')[0])}
        if contained_bags_and_count is None:
            contained_bags_and_count = contained_bag_and_count
        else:
            contained_bags_and_count.update(contained_bag_and_count)
    return contained_bags_and_count


def get_containing_to_contained_bags_map(rules):
    containing_to_contained_bags_map = {}
    for rule in rules:
        entry = {get_containing_bag(rule): get_contained_bags(rule)}
        if containing_to_contained_bags_map is None:
            containing_to_contained_bags_map = entry
        else:
            containing_to_contained_bags_map.update(entry)
    return containing_to_contained_bags_map


def get_num_contained_bags(bag, bags_map):
    if bags_map.__contains__(bag):
        bag_count = 0
        contained_bags = bags_map[bag]
        if contained_bags is None:
            return 0
        else:
            for contained_bag in contained_bags.keys():
                num_bags = contained_bags[contained_bag]
                num_contained_bags = get_num_contained_bags(contained_bag, bags_map)
                bag_count += num_bags + (num_bags * num_contained_bags)
            return bag_count
    return 0


def run():
    print()


class TestStringMethods(unittest.TestCase):

    def test_today(self):
        test_line = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
        test_line_with_none = 'dotted black bags contain no other bags.'
        assert_with_message('light red bag contain 1 bright white bag 2 muted yellow bag', pre_process_rule(test_line))
        assert_with_message('dotted black bag contain no other bag', pre_process_rule(test_line_with_none))
        assert_with_message('light red', get_containing_bag(test_line))
        assert_with_message({'bright white': 1, 'muted yellow': 2}, get_contained_bags(test_line))
        assert_with_message(None, get_contained_bags(test_line_with_none))
        assert_with_message({'light red': {'bright white': 1, 'muted yellow': 2}, 'dotted black': None},
                            get_containing_to_contained_bags_map([test_line, test_line_with_none]))

        test_input = ['shiny gold bags contain 2 dark red bags.',
                      'dark red bags contain 2 dark orange bags.',
                      'dark orange bags contain 2 dark yellow bags.',
                      'dark yellow bags contain 2 dark green bags.',
                      'dark green bags contain 2 dark blue bags.',
                      'dark blue bags contain 2 dark violet bags.',
                      'dark violet bags contain no other bags.']
        assert_with_message(126, get_num_contained_bags('shiny gold', get_containing_to_contained_bags_map(test_input)))
        assert_with_message(158493, get_num_contained_bags('shiny gold',
                                                        get_containing_to_contained_bags_map(get_input(7))))
        run()
