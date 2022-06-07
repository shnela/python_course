from functools import wraps


def duplicate_result_deco(f):
    pass


def multiply_result_deco(n):
    pass


@duplicate_result_deco
def duplicated_square(x):
    return x ** 2


@multiply_result_deco(2)
def multiply2_square(x):
    return x ** 2


@multiply_result_deco(3)
def multiply3_square(x):
    return x ** 2


class CustomException(Exception):
    pass


def retry_n_times(n):
    """Decorator catches `CustomException` nad retries running function ntimes
    every time it displays `attempt=<attempt_no>.
    After n times it rerises exception."""


@retry_n_times(3)
def raise_custom_exc():
    raise CustomException()


if __name__ == '__main__':
    assert duplicated_square(3) == 18
    assert duplicated_square.__name__ == 'duplicated_square'
    assert multiply2_square(3) == duplicated_square(3)
    assert multiply2_square.__name__ == 'multiply2_square'
    assert multiply3_square(3) == 27
    assert multiply3_square.__name__ == 'multiply3_square'

    raise_custom_exc()
