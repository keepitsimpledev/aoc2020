
def get_lines(filename):
    with open(filename, 'r', newline='\n') as inputfile:
        lines = inputfile.readlines()
        entries = []
        for entry in lines:
            entries = entries + [entry.strip('\n')]
        return entries
    return None


def assert_with_message(condition, expected, actual):
    assert condition, '\n\texpected: {}\n\tactual: {}'.format(expected, actual)
