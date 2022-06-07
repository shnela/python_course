def function_factory():
    x = 1

    def inner_function():
        # nonlocal x
        print(x)
        # x += 1

    return inner_function


if __name__ == '__main__':
    f = function_factory()
    f()
    f()
