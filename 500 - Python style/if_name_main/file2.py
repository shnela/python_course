print(f'file2 loaded ({__name__})')


def do_sth():
    print('do sth invoked')


if __name__ == '__main__':
    # it won't be executed when `file2` is imported as module
    print('file_2 in block if')
