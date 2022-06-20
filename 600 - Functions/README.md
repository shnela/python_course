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

## Default arguments
```python
def repeat(text, times=1):
    return text * times


print(repeat("foo", 2))
print(repeat("foo"))
```
[default_arguments.py](default_arguments.py)

Watch out for default mutable arguments: [default_mutable.py](default_mutable.py)

## Functions as first class citizens
> In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
Properties of first class functions:
> * A function is an instance of the Object type.
> * You can store the function in a variable.
> * You can pass the function as a parameter to another function.
> * You can return the function from a function.
> * You can store them in data structures such as hash tables, lists, …


```python
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))
```

```python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)
```

```python
# Python program to illustrate functions
# Functions can return another function
 
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))
```

## Nonlocal and global variables
* [nonlocal_variables.py](nonlocal_variables.py)
* [global_variables.py](global_variables.py)


## Python decorators
> Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
> without permanently modifying it. 

Example: [decorator_example.py](decorator_example.py)

Exercise: [decorator_exercise.py](decorator_exercise.py)


[Decorators in Python Geeks for Geeks]: https://www.geeksforgeeks.org/decorators-in-python/
