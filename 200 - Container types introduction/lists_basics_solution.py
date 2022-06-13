from random import randint


def print_elements(elements):
    print(f'List len: {len(elements)}')
    for e in elements:
        print(f'* {e}')


def sum_elements(elements):
    acc_sum = 0
    for e in elements:
        acc_sum += e
    return acc_sum


def min_element(elements):
    if not elements:
        return None
    min_val = elements[0]
    for e in elements:
        min_val = e if e < min_val else min_val
    return min_val


def avg_of_elements(elements):
    return sum_elements(elements) / len(elements)


if __name__ == '__main__':
    numbers = [randint(-5, 5) for _ in range(4)]
    print_elements(numbers)

    sum_val = sum_elements(numbers)
    print(f'SUM: {sum_val}')
    assert sum_val == sum(numbers)

    min_val = min_element(numbers)
    print(f'MIN: {min_val}')
    assert min_val == min(numbers)

    avg_val = avg_of_elements(numbers)
    print(f'AVG: {avg_val}')
    assert avg_val == sum(numbers) / len(numbers)

    # test empty sequences
    assert sum_elements([]) == 0
    assert min_element([]) is None
