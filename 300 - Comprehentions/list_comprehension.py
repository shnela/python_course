if __name__ == '__main__':
    even_numbers = list()
    assert even_numbers[0] == 2
    assert even_numbers[10] == 22
    assert even_numbers[-1] == 98
    assert len(even_numbers) == 49

    powers_of_2 = list()
    assert powers_of_2[0] == 1
    assert powers_of_2[10] == 1024
    assert powers_of_2[20] == 1048576
    assert powers_of_2[-1] == 633825300114114700748351602688
    assert len(powers_of_2) == 100
