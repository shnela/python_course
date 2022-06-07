from random import random


def random_numbers():
    print('start generator')
    while True:
        val = random()
        print(f'will yield {val}')
        yield val


def run_random_numbers():
    print(f'{random_numbers=}')
    rnd_gen = random_numbers()
    print(f'{rnd_gen=}')
    print(f'{next(rnd_gen)=}')
    print(f'{next(rnd_gen)=}')

    # but we can have two-way communication
    print(f'{rnd_gen.send(None)=}')
    print(f'{rnd_gen.send(42)=}')
    # rnd_gen.throw(Exception)
    # rnd_gen.close()
    # next(rnd_gen)


def inout_gen():
    print('init')
    ret_val = None
    while True:
        x = yield ret_val
        if x is not None:
            ret_val = x


def run_input_gen():
    inout_g = inout_gen()
    next(inout_g)

    print(f'{next(inout_g)}')
    print(f'{inout_g.send(22)}')
    print(f'{next(inout_g)}')


def exercise_gen(ret_val, times):
    """Return `ret_value` `times` times.
    If generator will receive some value from outside, update `ret_value`"""


def exercise1():
    """Make it pass"""
    g1 = exercise_gen(42, 3)
    assert next(g1) == 42
    assert g1.send('new val') == 'new val'
    assert next(g1) == 'new val'
    try:
        next(g1)
    except StopIteration:
        # ok
        pass
    else:
        raise Exception('Generator should be invalid')


def exercise2():
    """Update `exercise_gen`, so it will ignore all exceptions"""
    g1 = exercise_gen("I'll ignore errors", 300)
    assert next(g1) == "I'll ignore errors"
    assert g1.send('new val') == 'new val'
    assert g1.throw(Exception) == 'new val'
    assert next(g1) == 'new val'


if __name__ == '__main__':
    run_random_numbers()
    run_input_gen()
    exercise1()
    exercise2()
