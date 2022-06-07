def get_from_dict(d, key, default=None):
    """Implement dict.get using only `[]`"""
    try:
        return d[key]
    except KeyError:
        return default


def list_from_iterator(g):
    """Implement equivalent of `list(g)` using next() and StopIteration exception"""
    l = list()
    while True:
        try:
            l.append(next(g))
        except StopIteration:
            return l


if __name__ == '__main__':
    d = {'a': 1}
    assert get_from_dict(d, 'a') == 1
    assert get_from_dict(d, 'b') is None
    assert get_from_dict(d, 'b', default='fallback') == 'fallback'

    i = iter(range(10))
    next(i)
    assert list_from_iterator(i) == [1, 2, 3, 4, 5, 6, 7, 8, 9]