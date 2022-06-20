import os

fileToDump = 'duped_class.json'

from random import randint

class SomeClass:
    def __init__(self, ATTR1, attr2):
        self.ATTR1 = ATTR1
        self.attr2 = attr2

    def printAttributes(self):
        print(f'attrs: {self.ATTR1}, {self.attr2}')

class inheritedClass(SomeClass):
    def printAttributes(self):
        print(f"attrs: {self.attr2}, {self.ATTR1}")

def generate_int() -> str:
    return randint(0, 10)

if __name__ == '__main__':
    Number = generate_int()
    classInstance = SomeClass(Number, 'other attribute')
    classInstance.printAttributes()

    subclassInstance = inheritedClass(Number, "other attribute")
    subclassInstance.printAttributes()
