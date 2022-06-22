def deco(f):
    def inner_func(self, *args, **kwargs):
        print("will be run with deco")
        return f(self, *args, **kwargs)

    return inner_func


class Meta(type):
    def __init__(cls, name, bases, dct):
        for attr_name in dir(cls):
            if not attr_name.startswith('__') and callable(getattr(cls, attr_name)):
                setattr(cls, attr_name, deco(getattr(cls, attr_name)))


class A:
    def a(self):
        print("a")


class B(A, metaclass=Meta):
    def b(self):
        print("b")


if __name__ == '__main__':
    b = B()
    b.a()
    b.b()
