from random import random
from functools import partial


def multiply(a, b):
    return a * b


multiply_by2 = partial(multiply, 2)
assert multiply_by2(5) == 10


class Simple:
    def __init__(self, attr):
        self.attr = attr

    def multiplied_attr(self, x):
        return self.attr * x

    @classmethod
    def factory(cls):
        # return Simple(random())
        return cls(random())

    @staticmethod
    def out_of_context():
        return 42


if __name__ == '__main__':
    instance = Simple(10)
    print(instance.attr)
    instance.attr = 5
    print(instance.attr)
    instance.attr2 = 42
    print(instance.attr2)

    print(instance.multiplied_attr(10))
    print(Simple.multiplied_attr(instance, 10))
    print(partial(Simple.multiplied_attr, instance)(10))


