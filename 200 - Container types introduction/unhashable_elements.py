integer = 1
string = 'some text'
our_tuple = (integer, string)
our_list = [integer, string]
our_dict = {string: integer}
our_set = {string, integer}
our_frozenset = frozenset({integer, string})


if __name__ == '__main__':
    print(f'{hash(integer) = }')
    print(f'{hash(string) = }')
    print(f'{hash(our_tuple) = }')
    # print(f'{hash(our_list) = }')  # TypeError: unhashable type: 'list'
    # print(f'{hash(our_dict) = }')  # TypeError: unhashable type: 'dict'
    # print(f'{hash(our_set) = }'  # TypeError: unhashable type: 'set'
    print(f'{hash(our_frozenset) = }')

    # ...but
    # our_frozenset.add('other val')  # AttributeError: 'frozenset' object has no attribute 'add'
