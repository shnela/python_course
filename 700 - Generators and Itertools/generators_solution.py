from typing import Generator


def identify_generator(elements) -> Generator:
    yield from elements


def multiply_generator(elements, factor=1) -> Generator:
    """Return all values multiplied by factor"""
    yield from (e * factor for e in elements)


def custom_chain(*lists) -> Generator:
    """Merge all lists form tuple to one long generator"""
    for l in lists:
        yield from l


def limit(l, *, n) -> Generator:
    """Return first n elements from l"""
    g = (i for i in l)
    for _ in range(n):
        yield next(g)


def cycle(l) -> Generator:
    """Generate inifinite serie out of given list"""
    while True:
        yield from l


if __name__ == '__main__':
    short_list = [1, 2, 10]

    id_gen = identify_generator(short_list)
    assert list(id_gen) == short_list

    # Exercise1: make it works
    multiplied_gen = multiply_generator(short_list, 10)
    assert list(multiplied_gen) == [10, 20, 100]
    assert type(multiplied_gen) is type(id_gen)  # make sure you've created generator, not just returned list

    # Exercise2: make it works
    chained = custom_chain(short_list, [20], [30, 42])
    assert list(chained) == [1, 2, 10, 20, 30, 42]
    assert type(chained) is type(id_gen)  # make sure you've created generator, not just returned list

    # Exercise3: make it works
    limited = limit(short_list, n=2)
    assert list(limited) == [1, 2]
    assert type(limited) is type(id_gen)  # make sure you've created generator, not just returned list

    # Exercise4: make it works
    cycled = list(limit(cycle(short_list), n=900))
    assert cycled[:3] == [1, 2, 10]
    assert cycled[-3:] == [1, 2, 10]
    assert len(cycled) == 900
