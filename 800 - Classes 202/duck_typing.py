import abc
from collections import abc as cabc


class DummyIterable:
    def __iter__(self):
        yield 1
        yield 2
        yield 3


class GenericAirplane(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'flight') and callable(subclass.flight))


class A10:
    def flight(self):
        # https://www.youtube.com/watch?v=NvIJvPj_pjE
        return 'brrrrrrrrrrrrrt'


if __name__ == '__main__':
    l = [1, 2, 3]
    assert isinstance(l, cabc.Collection)
    assert isinstance(l, cabc.Iterable)

    dummy_iterable = DummyIterable()
    print(list(dummy_iterable))
    for e in dummy_iterable:
        print(e)
    assert isinstance(dummy_iterable, cabc.Iterable)

    # GenericAirplane
    a10 = A10()
    assert isinstance(a10, GenericAirplane)
