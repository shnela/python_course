# Basics

## Basic data types
[Basic Data Types in Python][]

### Integers
```python
print(12345)
print(2 ** 100)
# casting
string_val = '12'
integer_val = int(string_val)
```
Integers have unlimited range. [Python Max Int][]

#### Base systems
```python
val_8 = 0o10
val_16 = 0x10
val_2 = 0b10
```

### Floats
```python
print(12345.)
print(2. ** 100)
# casting
string_val = '.5'
integer_val = float(string_val)
```

> Almost all platforms represent Python float values as 64-bit “double-precision” values, according to the IEEE 754
> standard. In that case, the maximum value a floating-point number can have is approximately 1.8e10+308.
> Python will indicate a number greater than that by the string inf:
> 
> The closest a nonzero number can be to zero is approximately 5.0e10-324.
> Anything closer to zero than that is effectively zero.

### Boolean Type
```python
assert bool(42) is True
assert bool(0) is False
assert bool('text') is True
assert bool('') is False
assert bool([1, 2, 3]) is True
assert bool([]) is False
```

### Strings
```python
print('This string contains a single quote (\') character.')
print("This string contains a double quote (\") character.")
print('''This string has
a single (')
and a double (") quote.''')
```

## Formatting output
[Using % and .format() for great good!][] - "old" and "new" way of formatting strings.

But there's the newest: [Python 3's f-Strings][]
```python
name = 'Mark'
age = 41
print(f"He's {name}, next year he'll be {age + 1}")
```

### f-string features
#### [Formatted string literals]
```python
width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")
# output: "result:      12.35"
```
#### [f-strings support = for self-documenting expressions and debugging][]
```python
user = 'eric_idle'
member_since = date(1975, 7, 31)
print(f'{user=} {member_since=}')
# output: "user='eric_idle' member_since=datetime.date(1975, 7, 31)"

print(f'{theta=}  {cos(radians(theta))=:.3f}')
# output: "theta=30  cos(radians(theta))=0.866"
```
_new in pytyhon3.8_

## Unuseful or missing features
### Switch statement
Python doesn't have one.

[python_switch.py](python_switch.py)

### for else block
```python
for i in range(x):
    print(i)
    if i == 5:
        break
else:
    print('else block')
```
[for_else.py](for_else.py)

### while else block
```python
i = 0
while i < x:
    print(i)
    if i == 5:
        break
else:
    print('else block')
```
[while_else.py](while_else.py)

## Exception handling 
```python
try:
    # do something
    do_action()
    print('great - action done')
except ExceptionI as e:
    print('we have problem')
    raise
except (ExceptionII, ExceptionIII) as e:
    raise OtherException('explanation') from e
else:
    print('everything went fine - no problem')
finally:
    print('always invoke it, good place for closing files etc')
```
[exceptions.py](exceptions.py)

[Basic Data Types in Python]: https://realpython.com/python-data-types/
[Python Max Int]: https://www.pythonpool.com/python-max-int/
[Float type and its methods]: https://www.geeksforgeeks.org/python-float-type-and-its-methods/
[Using % and .format() for great good!]: https://pyformat.info/
[Python 3's f-Strings]: https://realpython.com/python-f-strings/
[Formatted string literals]: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
[f-strings support = for self-documenting expressions and debugging]: https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging