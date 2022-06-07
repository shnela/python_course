# Single line comment
"""Multi
line
comment
"""

int_val = 1
print(int_val)

float_val = 3.14
print(float_val)

text1 = 'dog\'s bone'
text2 = " and cat's one"
print(text1 + text2)

for i in range(3):
    print(str(i) + ' ' + text1)

counter = 0
while counter < 3:
    print(counter)
    counter += 1

if counter == 0:
    print('Not even started')
elif counter == 3:
    print('Everything is under control')
else:
    print("I'm confused.")

animals = ['cow', 'sheep']
print(animals)
animals.append('dog')
print(animals)

herd_count = {
    'cow': 1,
    'sheep': 5,
}
print(herd_count)
herd_count['dog'] = 1
herd_count['sheep'] -= 1
print(herd_count)


def square(x):
    return x ** 2


print(square(3))


class Dog:
    def __init__(self, fierceness):
        self.fierceness = fierceness

    def bark(self):
        print("Woof! " * self.fierceness)


Dog(2).bark()


class ItalianDog(Dog):
    def bark(self):
        print("Bau! " * self.fierceness)


ItalianDog(2).bark()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1))
print(factorial(100))
# https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion
# https://stackoverflow.com/questions/310974/what-is-tail-call-optimization
# TODO: use some tail recursion optimized algo
# print(factorial(10000))
