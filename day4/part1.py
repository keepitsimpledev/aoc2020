import unittest

from aoc_util import get_lines
from aoc_util import assert_with_message


def parse_entry_line(line: str):
    if line == '':
        return None
    else:
        parts = line.split(' ')
        labels = []
        for part in parts:
            labels = labels + [part.partition(':')[0]]
        return labels


def parse_passport_entries(lines):
    passports = []
    passport_labels = []
    for line in lines:
        info = parse_entry_line(line)
        if info is None:
            passports = passports + [passport_labels.copy()]
            passport_labels = []
        else:
            passport_labels = passport_labels + info
    if passport_labels is not None:
        passports = passports + [passport_labels.copy()]
    return passports


def passport_is_valid(labels):
    required_labels = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(item in labels for item in required_labels)


def find_number_of_valid_passports(passport_data):
    num_valid_passports = 0
    for passport in parse_passport_entries(passport_data):
        if passport_is_valid(passport):
            num_valid_passports = num_valid_passports + 1
    return num_valid_passports


def part1():
    passport_data = get_lines('day4.input')
    print('number of valid passports: {}'.format(find_number_of_valid_passports(passport_data)))


class TestStringMethods(unittest.TestCase):

    def test_part1(self):
        test_input = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
                      'byr:1937 iyr:2017 cid:147 hgt:183cm',
                      '',
                      'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
                      'hcl:#cfa07d byr:1929',
                      '',
                      'hcl:#ae17e1 iyr:2013',
                      'eyr:2024',
                      'ecl:brn pid:760753108 byr:1931',
                      'hgt:179cm',
                      '',
                      'hcl:#cfa07d eyr:2025 pid:166559648',
                      'iyr:2011 ecl:brn hgt:59in']
        assert parse_entry_line(test_input[0]) == ['ecl', 'pid', 'eyr', 'hcl']
        assert parse_entry_line(test_input[1]) == ['byr', 'iyr', 'cid', 'hgt']
        assert parse_entry_line(test_input[2]) is None
        assert_with_message(parse_entry_line(test_input[7]) == ['eyr'], ['eyr'], parse_entry_line(test_input[7]))
        assert_with_message(len(parse_passport_entries(test_input)) == 4, 4, len(parse_passport_entries(test_input)))
        assert parse_passport_entries(test_input)[0] == ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
        assert parse_passport_entries(test_input)[1] == ['iyr', 'ecl', 'cid', 'eyr', 'pid', 'hcl', 'byr']
        assert parse_passport_entries(test_input)[2] == ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']
        assert parse_passport_entries(test_input)[3] == ['hcl', 'eyr', 'pid', 'iyr', 'ecl', 'hgt']
        assert passport_is_valid(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'])
        assert not passport_is_valid(['iyr', 'ecl', 'cid', 'eyr', 'pid', 'hcl', 'byr'])
        assert passport_is_valid(['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt'])
        assert not passport_is_valid(['hcl', 'eyr', 'pid', 'iyr', 'ecl', 'hgt'])
        assert find_number_of_valid_passports(test_input) == 2
        part1()
