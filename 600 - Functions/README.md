# Functions

## Passing arguments by name
```python
def greetings(from_, to):
    print(f"{from_} greets {to}")
    

greetings("Alice", "Bob")
greetings("Alice", to="Bob")
greetings(from_="Alice", to="Bob")
greetings(to="Bob", from_="Alice")
```
[greetings.py](greetings.py)
    
## args and kwargs
```python
def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(1, 1, 2, 3, 5, foo="bar")
"""
(1, 1, 2, 3, 5)
{'foo': 'bar'}
"""
```
[function_args.py](function_args.py)
    
## Passing args and kwargs
```python
def greetings(from_, to):
    print(f"{from_} greets {to}")


tuple_parameters = ("Alice", "Bob")
greetings(*tuple_parameters)

dict_parameters = {
    "from_": "Alice",
    "to": "Bob"
}
greetings(**dict_parameters)
```
[greetings_passing_args_and_kwargs.py](greetings_passing_args_and_kwargs.py)

## Nonlocal and global variables
* [nonlocal_variables.py](nonlocal_variables.py)
* [global_variables.py](global_variables.py)

## Default arguments
```python
def repeat(text, times=1):
    return text * times


print(repeat("foo", 2))
print(repeat("foo"))
```
[default_arguments.py](default_arguments.py)

Watch out for default mutable arguments: [default_mutable.py](default_mutable.py)


## Python decorators
> Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
> without permanently modifying it. 

Example: [decorator_example.py](decorator_example.py)

Exercise: [decorator_exercise.py](decorator_exercise.py)