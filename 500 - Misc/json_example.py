"""Change file name to json"""
import json
from decimal import Decimal


def direct_conversion(obj):
    obj_json = json.dumps(obj)
    print(obj_json)
    print(json.loads(obj_json))


def file_conversion(obj, filename):
    with open(filename, 'w') as f:
        json.dump(obj, f)
    with open(filename, 'r') as f:
        print(json.load(f))


if __name__ == '__main__':
    l1 = [1, 2, 3.14, 'simple_text']
    direct_conversion(l1)
    file_conversion(l1, './list.json')

    l1.append(Decimal(10))
    direct_conversion(l1)
