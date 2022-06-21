class Strange:
    def __init__(self, idx, text):
        self.idx = idx
        self.text = text

    def __str__(self):
        return f'{self.text[:self.idx]}({self.text[self.idx]}){self.text[self.idx + 1:]}'

    def __add__(self, other):
        if isinstance(other, int):
            return Strange(
                idx=self.idx + other,
                text=self.text,
            )
        raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'")

    def __len__(self):
        return len(self.text)

    def __iter__(self):
        yield self.idx
        yield from self.text

    def __next__(self):
        if self.idx < len(self.text):
            val = self.text[self.idx]
            self.idx += 1
            return val
        raise StopIteration()

    # def __getattribute__(self, item):
    #     pass

    def __getattr__(self, item):
        return f'Fake {item} attribute'

    def __getitem__(self, item):
        print(f'item {item} accessed by []')

    def __sub__(self, other):
        print('hehe')


if __name__ == '__main__':
    strange = Strange(2, 'what now?')
    print(strange)
    # print(strange + Strange(3, 'and then?'))
    print(strange + 3)
    print(hash(strange))
    print(len(strange))
    print(list(strange))

    print(next(strange))
    strange += 5
    print(strange)
    print(next(strange))
    try:
        print(next(strange))
    except StopIteration:
        print('Iterator exhausted')

    print(strange.idx, strange.missing_attr)

    print(strange[1])
    print(strange[1:-1:3])
