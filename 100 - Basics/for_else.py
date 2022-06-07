"""for else blocks are counterintuitive, please do not use them
"""


def print_range(x: int):
    print('Start: ', end=' ')
    for i in range(x):
        print(i, end=' ')
        if i == 5:
            break
    else:
        print('(invoked only when there was no break)', end='')
    print()


if __name__ == '__main__':
    print_range(0)
    print_range(2)
    print_range(5)
    print_range(6)
    print_range(10)
