print('start loading code')


def append_1_wrong(l=list()):
    print(f'Wrong Before {l}')
    l.append(1)
    print(f'Wrong After {l}')


def append_1_ok(l=None):
    l = list() if l is None else l
    print(f'Good Before {l}')
    l.append(1)
    print(f'Good After {l}')


if __name__ == '__main__':
    append_1_wrong()
    append_1_wrong()

    append_1_ok()
    append_1_ok()
