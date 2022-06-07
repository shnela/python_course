# [List Comprehension][]

## Example
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [f for f in fruits if "a" in f]
assert fruits_with_a == ['apple', 'banana', 'mango']
```

## Syntax
```
newlist = [expression for item in iterable if condition == True]
```

## Other comprehensions

### Dict
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = {f: len(f) for f in fruits if "a" in f}
assert fruits_with_a == {'apple': 5, 'banana': 6, 'mango': 5}
```

### Set
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = {f for f in fruits if "a" in f}
assert fruits_with_a == {'apple', 'banana', 'mango'}
```

### Generator
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = (f for f in fruits if "a" in f)
assert list(fruits_with_a) == ['apple', 'banana', 'mango']
```

## Constructing collections

| Object type | Constructor |      | Comprehension                    |
|-------------|-------------|------|----------------------------------|
| list        | `list()`    | `[]` | `[e for e in range(10)]`         |
| dict        | `dict()`    | `{}` | `{e: len(e) for e in range(10)}` |
| set         | `set()`     |      | `{e for e in range(10)}`         |
| tuple       | `tuple()`   | `()` |                                  |
| generator   |             |      | `(e for e in range(10))`         |


## Exercises
* [measure_words_length.py](measure_words_length.py)
* [count_words.py](count_words.py)

[List Comprehension]: https://www.w3schools.com/python/python_lists_comprehension.asp
