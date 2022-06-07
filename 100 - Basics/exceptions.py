def get_from_dict(d, key, default=None):
    """Implement dict.get using only `[]`"""


def list_from_iterator(g):
    """Implement equivalent of `list(g)` using next() and StopIteration exception"""


if __name__ == '__main__':
    d = {'a': 1}
    assert get_from_dict(d, 'a') == 1
    assert get_from_dict(d, 'b') is None
    assert get_from_dict(d, 'b', default='fallback') == 'fallback'

    i = iter(range(10))
    next(i)
    assert list_from_iterator(i) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
