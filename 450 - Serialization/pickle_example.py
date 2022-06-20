import pickle
from decimal import Decimal


def direct_conversion(obj):
    obj_json = pickle.dumps(obj)
    deserialized_object = pickle.loads(obj_json)
    return deserialized_object


def file_conversion(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
    with open(filename, 'rb') as f:
        deserialized_object = pickle.load(f)
    return deserialized_object


if __name__ == '__main__':
    elements = [1, 2, 3.14, 'simple_text']
    direct_conversion(elements)
    direct_conversion(elements)
    file_conversion(elements, './list.json')

    """
    What's the problem with float?
    >>> 1.1 + 2.2
    3.3000000000000003
    >>> Decimal('1.1') + Decimal('2.2')
    Decimal('3.3')
    """

    elements.append(Decimal(10))
    pickled_elements = pickle.dumps(elements)
    print(pickled_elements)
