from typing import List, Tuple


def detect_new_and_deleted_entries(prev_elements, current_elements) -> Tuple[List, List]:
    """Returns tuple of two lists: (<list of new items>, <list of deleted items>)"""
    return list(), list()


def detect_non_modified_elements(prev_elements, current_elements) -> List:
    """Returns list of elements common for both `prev_elements` and `current_elements`"""
    return list()


if __name__ == '__main__':
    old_values = {'Alice', 'Bob to Del', 'Chris'}
    new_values = {'Alice', 'Chris', 'Dave New'}

    # Exercise 1: make it pass
    assert detect_new_and_deleted_entries(old_values, new_values) == (['Dave New'], ['Bob to Del'])

    # Exercise 2:
    assert set(detect_non_modified_elements(old_values, new_values)) == {'Alice', 'Chris'}
    # we can't be sure of order of elements
    # assert detect_non_modified_elements(old_values, new_values) == ['Alice', 'Chris']

    # Exercise 3: make it pass when list was passed instead of set
    assert detect_new_and_deleted_entries(list(old_values), list(new_values)) == (['Dave New'], ['Bob to Del'])
    assert set(detect_non_modified_elements(list(old_values), list(new_values))) == {'Alice', 'Chris'}
