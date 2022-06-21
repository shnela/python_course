"""https://realpython.com/python-descriptors/
"""


class NonNegativeValue:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value


class Ball:
    def __init__(self, weight, diameter):
        self._weight = weight
        self._diameter = diameter

    weight = NonNegativeValue()
    diameter = NonNegativeValue()


if __name__ == '__main__':
    a = Ball(weight=10, diameter=5)
    print(a.weight)
    print(a.diameter)
    a.weight = 11
    print(a.weight)
