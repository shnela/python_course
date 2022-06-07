def test_order_of_accessing_dict_data():
    """
    ord('a') == 97
    chr(97) == 'a'
    :return:
    """
    letters = dict()
    for ascii_no in range(ord('A'), ord('z') + 1):
        letters[chr(ascii_no)] = ascii_no

    for letter, ascii_no in letters.items():
        print(letter, ascii_no)


if __name__ == '__main__':
    test_order_of_accessing_dict_data()
