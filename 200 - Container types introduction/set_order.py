def test_order_of_accessing_set_data():
    """
    ord('a') == 97
    chr(97) == 'a'
    :return:
    """
    letters = set()
    for ascii_no in range(ord('A'), ord('z') + 1):
        letters.add(chr(ascii_no))

    for letter in letters:
        print(letter)


if __name__ == '__main__':
    test_order_of_accessing_set_data()
