if __name__ == '__main__':
    animals = [
        'Brown Recluse Spider',
        'Camels',
        'Cape Gannet Bird',
        'Chickens',
        'Chimpanzee',
        'Cuviers Dwarf Caimans',
        'Dog',
    ]

    # Exercise 1: make it pass
    words_with_len = dict()
    assert words_with_len == {
        'Brown Recluse Spider': 20, 'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10,
        'Cuviers Dwarf Caimans': 21, 'Dog': 3
    }

    # Exercise 2: make it pass using `words_with_len` dict (filter elements with odd values)
    words_with_even_len = dict()
    assert words_with_even_len == {
        'Brown Recluse Spider': 20, 'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10
    }

    # Exercise 3: make it pass using `words_with_len` dict
    assert 'Confluence'.startswith('Conf')
    # Filter words_with_len where key starts with 'prefix_to_filter'
    prefix_to_filter = 'C'
    words_with_prefix = dict()
    assert words_with_prefix == {
        'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10, 'Cuviers Dwarf Caimans': 21
    }
    prefix_to_filter = 'Ch'
    words_with_prefix2 = dict()
    assert words_with_prefix2 == {
        'Chickens': 8, 'Chimpanzee': 10,
    }
