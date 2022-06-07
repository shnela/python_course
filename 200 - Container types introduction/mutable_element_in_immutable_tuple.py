if __name__ == '__main__':
    # give tuple
    t = (1, 'a', [])

    # you can't explicitly modify it's elements
    # t[0] += 1  # TypeError: 'tuple' object does not support item assignment
    # t[2] += [1]  # TypeError: 'tuple' object does not support item assignment

    # ...but
    t[2].append(1)  # works...
    print(t)

""""Bonus from Fluent Python by Luciano_Ramalho
Corner case in console:

>>> t = (1, 'a', [])
>>> t[2] += [1]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 'a', [1])
>>> import dis
>>> dis.dis('t[2] += [1]')
  1           0 LOAD_NAME                0 (t)
              2 LOAD_CONST               0 (2)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_CONST               1 (1)
             10 BUILD_LIST               1
             12 INPLACE_ADD
             14 ROT_THREE
             16 STORE_SUBSCR
             18 LOAD_CONST               2 (None)
             20 RETURN_VALUE
             
# https://docs.python.org/3/library/dis.html#python-bytecode-instructions
"""