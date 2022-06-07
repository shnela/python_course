def print_elements(elements):
    print(f'List len: {len(elements)}')
    for e in elements:
        print(f'* {e}')


def sum_elements(elements):
    """Return 0 if list is empty"""


def min_element(elements):
    """Return None if list is empty"""


def avg_of_elements(elements):
    pass


if __name__ == '__main__':
    numbers = list(range(10))
    print_elements(numbers)

    sum_val = sum_elements(numbers)
    print(f'SUM: {sum_val}')

    min_val = min_element(numbers)
    print(f'MIN: {min_val}')

    avg_val = avg_of_elements(numbers)
    print(f'AVG: {avg_val}')
