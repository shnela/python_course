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
    words_with_len = {animal: len(animal) for animal in animals}
    assert words_with_len == {
        'Brown Recluse Spider': 20, 'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10,
        'Cuviers Dwarf Caimans': 21, 'Dog': 3
    }

    # Exercise 2: make it pass
    words_with_even_len = {word: word_len for word, word_len in words_with_len.items() if not word_len % 2}
    assert words_with_even_len == {
        'Brown Recluse Spider': 20, 'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10
    }

    # Exercise 3: make it pass
    assert 'Confluence'.startswith('Conf')
    # Filter words_with_len where key starts with 'C'
    words_with_prefix = {word: word_len for word, word_len in words_with_len.items() if word.startswith('C')}
    assert words_with_prefix == {
        'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10, 'Cuviers Dwarf Caimans': 21
    }
