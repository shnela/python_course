# Functions
    
## Passing arguments examples
```python
    # passing by position or name
    real_life_example('val1', 'val2', confusing_parameter=True)
    # following calls are equivalent
    mixed_model('val1', 'val2', kwarg1=1)
    mixed_model(*['val1', 'val2'], **dict(kwarg1=1))
```
[function_args.py](function_args.py)

## Python decorators
TODO: add better decorator explanation
```python
def deco(f):
    print('Decorator starts')

    @wraps(f)
    def inner_func(*args, **kwargs):
        print(f'Inner starts')
        result = f(*args, **kwargs)
        print(f'Inner ends')
        return result

    print('Decorator ends')
    return inner_func


@deco('paramter value')
def simple_print_args(arg1, arg2):
    print(arg1)
    print(arg2)
```
Example: [decorator_example.py](decorator_example.py)

Exercise: [decorator_exercise.py](decorator_exercise.py)

Watch out for default mutable arguments: [default_mutable.py](default_mutable.py)
