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
    assert text[-8:16] == 'old'  # it works, but doesn't look good

    step_by_2 = 'Level'[::2]
    assert step_by_2 == 'Lvl'

    one_two_three = [1, 2, 3]
    assert one_two_three[1] == 2
    assert one_two_three[1:2] == [2]
    one_two_three[1:2] = [10, 20, 30]
    assert one_two_three == [1, 10, 20, 30, 3]

    reverse_level = 'Level'[:]  # Exercise
    assert reverse_level == 'leveL'

    with_bang = list(text)
    # with_bang[] =   # Exercise
    assert ''.join(with_bang) == "There was an old dog!"

    with_cat = list(text)
    # with_cat[] = # Exercise
    assert ''.join(with_cat) == "There was an old cat."

    numbers = list(range(10))
    even_numbers = numbers[:]  # Exercise
    assert even_numbers == [0, 2, 4, 6, 8]

    even_numbers = numbers[:]  # Exercise
    assert even_numbers == [1, 3, 5, 7, 9]
