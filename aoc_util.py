import requests


__2020cookie\
    = 'session=53616c7465645f5f219f321fd9f4d85a83f65067516bfabc5cc2159fb9b01640da4e6955487e8e404ea2fe31dc063b2e'


@DeprecationWarning
def get_lines(filename):
    with open(filename, 'r', newline='\n') as inputfile:
        lines = inputfile.readlines()
        entries = []
        for entry in lines:
            entries = entries + [entry.strip('\n')]
        return entries
    return None


def assert_with_message(expected, actual):
    assert expected == actual, '\n\texpected: {}\n\tactual: {}'.format(expected, actual)


# TODO: update old days where input processing was done
def get_input(day: int):
    url = 'https://adventofcode.com/2020/day/{}/input'.format(day)
    response = requests.get(url, headers={'Cookie': __2020cookie})
    out = response.content.decode().split('\n')
    return out[:len(out) - 1]


def input_strings_to_ints(strings_in):
    return list(map(int, strings_in))
