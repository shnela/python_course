"""There's no such thing as switch statemtnt in python"""


def digit_to_text(digit: int) -> str:
    if digit == 1:
        return 'one'
    elif digit == 2:
        return 'two'
    else:
        return 'definitely nor one or two'


if __name__ == '__main__':
    print(digit_to_text(1))
