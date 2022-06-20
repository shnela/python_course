from file2 import do_sth

print(f'file1 loaded ({__name__})')

if __name__ == '__main__':
    print('file_1 in block if')
    do_sth()
