def display_enumerated_lines(filename):
    """Display lines of files with line number as prefix
    use `enumerate` function"""

def reverse_lines_y(filename):
    """Reads data from `<filename>` and writes reversed lines to file `<filename>_reversed_y'
    e.g.
    a b  >  b a
    c d  >  d c
    """
    with open(filename) as in_f, open(f'{filename}_reversed_y', 'w') as out_f:
        in_lines = in_f.read().splitlines()
        out_f.write('\n'.join(in_lines[::-1]))


def reverse_lines_x(filename):
    """Reads data from `<filename>` and writes reversed lines to file `<filename>_reversed_x'
    e.g.
    a b  >  c d
    c d  >  a b
    """
    with open(filename) as in_f, open(f'{filename}_reversed_x', 'w') as out_f:
        in_lines = in_f.read().splitlines()
        out_f.write('\n'.join((l[::-1] for l in in_lines)))


def reverse_lines(filename):
    """Reads data from `<filename>` and writes reversed lines to file `<filename>_reversed'
    e.g.
    a b  >  d c
    c d  >  b a
    """
    with open(filename) as in_f, open(f'{filename}_reversed', 'w') as out_f:
        in_lines = in_f.read().splitlines()
        out_f.write('\n'.join((l[::-1] for l in in_lines[::-1])))


if __name__ == '__main__':
    filename = './data/matrix'

    display_enumerated_lines(filename)
    reverse_lines_x(filename)
    reverse_lines_y(filename)
    reverse_lines(filename)
