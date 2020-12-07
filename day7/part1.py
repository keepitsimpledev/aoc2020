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


def can_contain_bag(bag, containing_bag, bags_map):
    if bags_map.__contains__(containing_bag):
        contained_bags = bags_map[containing_bag]
        if contained_bags is None:
            return False
        else:
            for contained_bag in contained_bags.keys():
                if contained_bag == bag:
                    return True
                elif can_contain_bag(bag, contained_bag, bags_map):
                    return True
    return False


def get_num_containing_bags(bag, rules):
    containing_to_contained_bags_map = get_containing_to_contained_bags_map(rules)
    containing_bags = []
    for containing_bag in containing_to_contained_bags_map.keys():
        if can_contain_bag(bag, containing_bag, containing_to_contained_bags_map):
            containing_bags += [containing_bag]
    return len(containing_bags)


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
        containing_to_contained_bags_map = get_containing_to_contained_bags_map([test_line, test_line_with_none])
        assert_with_message(True, can_contain_bag('bright white', 'light red', containing_to_contained_bags_map))
        assert_with_message(False, can_contain_bag('vibrant plum', 'light red', containing_to_contained_bags_map))
        assert_with_message(False, can_contain_bag('bright white', 'dotted black', containing_to_contained_bags_map))

        test_input = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
                      'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
                      'bright white bags contain 1 shiny gold bag.',
                      'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
                      'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
                      'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
                      'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
                      'faded blue bags contain no other bags.',
                      'dotted black bags contain no other bags.']
        assert_with_message(4, get_num_containing_bags('shiny gold', test_input))
        assert_with_message(235, get_num_containing_bags('shiny gold', get_input(7)))
        run()
