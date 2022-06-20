from functools import wraps


def deco(f):
    print('Decorator starts')

    # @wraps(f)
    def inner_func():
        print(f'Inner starts')
        f()
        print(f'Inner ends')

    print('Decorator ends')
    return inner_func


# @deco
def main_function():
    print("Inner fu")


decorated_main_function = deco(main_function)


if __name__ == '__main__':
    decorated_main_function()

    # our_main_function('arg1_val')

    # print(decorated_main_function.__name__)
