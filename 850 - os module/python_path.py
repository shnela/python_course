import os


if __name__ == '__main__':
    print('== base ==')
    print(__file__)
    current_dir = os.path.dirname(__file__)
    print(current_dir)

    # on Windows it mixes slashes and backslashes
    print('== raw modified ==')
    print(os.path.join(current_dir, '..'))
    print(os.path.join(current_dir, 'subdir1', 'subdir2'))

    # `os.path.abspath` will do the job
    print('== abspath wrapped ==')
    print(os.path.abspath(os.path.join(current_dir, '..')))
    print(os.path.abspath(os.path.join(current_dir, 'subdir1', 'subdir2')))
