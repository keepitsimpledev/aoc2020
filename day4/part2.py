import unittest
import re

from aoc_util import get_lines
from aoc_util import assert_with_message


def parse_entry_line(line: str):
    if line == '':
        return None
    else:
        parts = line.split(' ')
        labels = {}
        for part in parts:
            label = {part.partition(':')[0]: part.partition(':')[2]}
            if labels == {}:
                labels = label
            else:
                combined = labels | label
                labels = combined
        return labels


def parse_passport_entries(lines):
    passports = []
    passport_labels = {}
    for line in lines:
        info = parse_entry_line(line)
        if info is None:
            passports = passports + [passport_labels.copy()]
            passport_labels = {}
        else:
            passport_labels = passport_labels | info
    if passport_labels is not None:
        passports = passports + [passport_labels.copy()]
    return passports


def passport_is_valid(info):
    required_labels = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    try:
        assert all(item in list(info.keys()) for item in required_labels)
        assert 1920 <= int(info['byr']) <= 2002
        assert 2010 <= int(info['iyr']) <= 2020 <= int(info['eyr']) <= 2030
        height_raw = info['hgt']
        height_length = len(height_raw)
        assert height_length >= 3 and height_raw[height_length - 2: height_length] in ('cm', 'in')
        height = int(height_raw[:height_length - 2])
        unit = height_raw[height_length - 2: height_length]
        if unit == 'cm':
            assert 150 <= height <= 193
        else:
            assert 59 <= height <= 76
        assert re.match('^#[a-f0-9]{6}$', info['hcl'])
        assert info['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        assert re.match('^\d{9}$', info['pid'])
    except AssertionError:
        return False
    return True


def find_number_of_valid_passports(passport_data):
    num_valid_passports = 0
    for passport in parse_passport_entries(passport_data):
        if passport_is_valid(passport):
            num_valid_passports = num_valid_passports + 1
    return num_valid_passports


def part2():
    passport_data = get_lines('day4.input')
    print('number of valid passports: {}'.format(find_number_of_valid_passports(passport_data)))


class TestStringMethods(unittest.TestCase):

    def test_part2(self):
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
        assert_with_message(
            parse_entry_line(test_input[0]) == {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd'},
            {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd'},
            parse_entry_line(test_input[0]))
        assert parse_entry_line(test_input[1]) == {'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
        assert parse_entry_line(test_input[2]) is None
        assert_with_message(parse_entry_line(test_input[7]) == {'eyr': '2024'}, {'eyr': '2024'}, parse_entry_line(test_input[7]))
        assert_with_message(len(parse_passport_entries(test_input)) == 4, 4, len(parse_passport_entries(test_input)))
        assert parse_passport_entries(test_input)[0] == {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
                                                         'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147',
                                                         'hgt': '183cm'}
        assert parse_passport_entries(test_input)[3] == {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648',
                                                         'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}
        assert passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                  'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1919',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '2003',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2009', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2021', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2019', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2031', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '149cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '194cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '58in'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '77in'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#wffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffdd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'yel', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '0860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert not passport_is_valid({'ecl': 'gry', 'pid': '0033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937',
                                      'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
        assert find_number_of_valid_passports(test_input) == 2
        invalid = ['eyr:1972 cid:100',
                   'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
                   '',
                   'iyr:2019',
                   'hcl:#602927 eyr:1967 hgt:170cm',
                   'ecl:grn pid:012533040 byr:1946',
                   '',
                   'hcl:dab227 iyr:2012',
                   'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
                   '',
                   'hgt:59cm ecl:zzz',
                   'eyr:2038 hcl:74454a iyr:2023',
                   'pid:3556412378 byr:2007']
        assert find_number_of_valid_passports(invalid) == 0
        valid = ['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
                 'hcl:#623a2f',
                 '',
                 'eyr:2029 ecl:blu cid:129 byr:1989',
                 'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
                 '',
                 'hcl:#888785',
                 'hgt:164cm byr:2001 iyr:2015 cid:88',
                 'pid:545766238 ecl:hzl',
                 'eyr:2022',
                 '',
                 'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']
        assert find_number_of_valid_passports(valid) == 4
        part2()
