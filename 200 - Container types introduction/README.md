# Container types

## List
```python
# list of only integers
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of only strings
b = ['hello', 'john', 'reese']
print(b)

# list of both integers and strings
c = ['hey', 'you', 1, 2, 3, 'go']
print(c)

# index are 0 based. this will print a single character
print(c[1])  # this will print 'you' in list c

# constructing list
letters = list('some text')
print(letters)
# list is mutable
letters[0] = 's replacement'
print(letters)
```

Let's do [lists_basics.py](./lists_basics.py)

### List [Slicing][]
```python
a[start:stop]  # items start through stop-1
a[start:stop:step]  # items start through stop-1 with step
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```
Exercise: [slicing.py](./slicing.py)

## Tuple
```python
# tuple having only integer type of data.
a = (1, 2, 3, 4)
print(a)  # prints the whole tuple

# tuple having multiple types of data.
b = ('hello', 1, 2, 3, 'go')
print(b)  # prints the whole tuple

# index of tuples are also 0 based.
print(b[4])  # this prints a single element in a tuple, in this case 'go'

# constructing tuple
letters = tuple('some text')
print(letters)
# list is mutable
letters[0] = 's replacement'  # Will throw TypeError
```

### [Tuples unpacking](https://www.w3schools.com/python/python_tuples_unpack.asp)

```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
# (green, *tropic, *red) = fruits  # SyntaxError: multiple starred expressions in assignment
```

### Other about tuple
[mutable_element_in_immutable_tuple.py](mutable_element_in_immutable_tuple.py)

## Dict
```python
# a sample dictionary variable
a = {1: 'first name', 2: 'last name', 'age': 33}
print(a)  # prints the whole dict

# print value having key=1
print(a[1])
# print value having key=2
print(a[2])
# print value having key='age'
print(a['age'])
```

### Accessing dict elements
```python
d = {
    'one': 1,
}
assert d['one'] == 1    
# d['three']  # KeyError: 'three'
assert d.get('one') == 1
assert d.get('three') is None
assert d.get('three', 'fallback val') == 'fallback val'
```

### Iterating over dict
```python
d = {
    'one': 1,
    'two': 2,
}
assert list(d) == list(d.keys()) == ['one', 'two']
assert list(d.values()) == [1, 2]
assert list(d.items()) == [('one', 1), ('two', 2)]

# Tuple unpacking is useful
for k, v in d.values():
    print(k, v)
```

### Exercises:
* [measure_words_length.py](measure_words_length.py)
* [count_words.py](count_words.py)

### [dictionaries ordered since Python 3.6+][]
> They are insertion ordered. As of Python 3.6, for the CPython implementation of Python,
> dictionaries remember the order of items inserted.
> This is considered an implementation detail in Python 3.6; you need to use OrderedDict if you want insertion
> ordering that's guaranteed across other implementations of Python (and other ordered behavior).
>
> As of Python 3.7, this is no longer an implementation detail and instead becomes a language feature.

Look at [dict_order.py](./dict_order.py).


## [Set][]
```python
one_set = set()
one_set.add(1)
one_set.add(1)
print(one_set)
# {1}

initialized_set = {1, 2, 1}
print(initialized_set)
# {1, 2}

assert one_set < initialized_set  # one_set is subset of initialized_set
assert initialized_set - one_set == {2}
assert initialized_set & one_set == {1}
assert initialized_set | one_set == {1, 2}
```

### But set isn't ordered
[`set_order.py`](set_order.py)

### Exercise
[`set_example.py`](set_example.py)

## Hashable / unhashable
All set items and dictionary keys must be hashable.
[`unhashable_elements.py`](unhashable_elements.py)

[dictionaries ordered in Python 3.6+]: https://stackoverflow.com/a/39980744/1565454
[Slicing]: https://stackoverflow.com/a/509295/1565454
[Set]: https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
