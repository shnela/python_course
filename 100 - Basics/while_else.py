"""while else blocks are counterintuitive, please do not use them
"""


def print_range(x: int):
    print('Start: ', end=' ')
    i = 0
    while i < x:
        print(i, end=' ')
        if i == 5:
            break
        i += 1
    else:
        print('While condition is no longer true', end='')
    print()


if __name__ == '__main__':
    print_range(0)
    print_range(2)
    print_range(5)
    print_range(6)
    print_range(10)
