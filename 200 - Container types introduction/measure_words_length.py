from typing import Dict, List


def measure_lengths(words: List[str]) -> Dict[str, int]:
    return dict()


def filter_words_with_even_length(words_with_len: Dict[str, int]) -> Dict[str, int]:
    return words_with_len


def filter_words_with_prefix(words_with_len: Dict[str, int], required_prefix: str) -> Dict[str, int]:
    return words_with_len


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
    words_with_len = measure_lengths(animals)
    assert words_with_len == {
        'Brown Recluse Spider': 20, 'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10,
        'Cuviers Dwarf Caimans': 21, 'Dog': 3
    }

    # Exercise 2: make it pass
    words_with_even_len = filter_words_with_even_length(words_with_len)
    assert words_with_even_len == {
        'Brown Recluse Spider': 20, 'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10
    }

    # Exercise 3: make it pass
    assert 'Confluence'.startswith('Conf')
    words_with_prefix1 = filter_words_with_prefix(words_with_len, required_prefix='C')
    assert words_with_prefix1 == {
        'Camels': 6, 'Cape Gannet Bird': 16, 'Chickens': 8, 'Chimpanzee': 10, 'Cuviers Dwarf Caimans': 21
    }
    words_with_prefix2 = filter_words_with_prefix(words_with_len, required_prefix='Ch')
    assert words_with_prefix2 == {
        'Chickens': 8, 'Chimpanzee': 10,
    }
