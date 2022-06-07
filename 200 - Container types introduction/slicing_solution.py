def print_indexes(text):
    position_width = 3
    for i in range(len(text)):
        print(f'{i:{position_width}}', end=' ')
    print()
    for i in range(len(text)):
        negative_index = -(len(text) - i)
        print(f'{negative_index:{position_width}}', end=' ')
    print()
    text_without_spaces = text.replace(' ', '_')
    for l in text_without_spaces:
        print(f'{l:>{position_width}}', end=' ')
    print()


if __name__ == '__main__':
    text = "There was an old dog."
    """python
    list(text)
    # ['T', 'h', 'e', 'r', 'e', ' ', 'w', 'a', 's', ' ', 'a', 'n', ' ', 'o', 'l', 'd', ' ', 'd', 'o', 'g', '.']
    '-'.join(list(text))
    # 'T-h-e-r-e- -w-a-s- -a-n- -o-l-d- -d-o-g-.'
    """
    print_indexes(text)

    assert text[0] == 'T'
    assert text[-2] == 'g'
    assert text[13:16] == 'old'
    assert text[-8:-5] == 'old'

    reverse_level = 'Level'[::-1]
    assert reverse_level == 'leveL'

    with_bang = list(text)
    with_bang[-1] = '!'
    assert ''.join(with_bang) == "There was an old dog!"

    with_cat = list(text)
    with_cat[-4:-1] = 'cat'
    assert ''.join(with_cat) == "There was an old cat."

    numbers = list(range(10))
    even_numbers = numbers[::2]  # Exercise
    assert even_numbers == [0, 2, 4, 6, 8]

    even_numbers = numbers[1::2]  # Exercise
    assert even_numbers == [1, 3, 5, 7, 9]
