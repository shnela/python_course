from functools import wraps


def parametrized_deco(paramter):
    def inner_deco(f):
        print('Decorator starts')

        @wraps(f)
        def inner_func(*args, **kwargs):
            print(f'Inner starts {paramter}')
            result = f(*args, **kwargs)
            print(f'Inner ends {paramter}')
            return result

        print('Decorator ends')
        return inner_func
    return inner_deco


@parametrized_deco('paramter value')
def simple_print_args(arg1, arg2):
    print(arg1)
    print(arg2)


if __name__ == '__main__':
    simple_print_args('arg1_val', 'arg2_val')
