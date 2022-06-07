def sample_function(arg):
    print(arg)


def get_all_args(*args):
    print(args)


def get_all_kwargs(**kwargs):
    print(kwargs)


def mixed_model(var1, *remaining_args, kwarg1, **remining_kwargs):
    print(var1)
    print(remaining_args)
    print(kwarg1)
    print(remining_kwargs)


def real_life_example(arg1, arg2, *, confusing_parameter=False):
    """confusing parameter has to be ALWAYS passed explicitly"""


if __name__ == '__main__':
    sample_function('val1')
    sample_function(arg='val1')
    get_all_args('val1', 'val2')
    # get_all_args('val1', some_fun_var='val2')
    # get_all_kwargs('val1')
    get_all_kwargs(some_fun_var='val1', some_fun_var2='val2')
    mixed_model('val1', 'val2', kwarg1=1)
    mixed_model(*['val1', 'val2'], **dict(kwarg1=1))

    # real_life_example('val1', 'val2', True)
    real_life_example('val1', 'val2', confusing_parameter=True)
