class Ball:
    def __init__(self, weight, diameter):
        self._weight = weight
        self.__diameter = diameter

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError('Value should be greater than 0')
        self._weight = value

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError('Value should be greater than 0')
        self.__diameter = value


if __name__ == '__main__':
    a = Ball(weight=10, diameter=5)
    print(a.weight)
    a.weight = 11
    print(a.weight)

    # but
    a._weight = -1
    print(a.weight)

    #
    # a.__diameter = -1
    # a._Ball__diameter = -1
    print(a.diameter)
