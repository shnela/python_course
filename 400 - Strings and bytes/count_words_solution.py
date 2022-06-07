import re
from collections import defaultdict


def remove_non_alpha_characters(text):
    regex = re.compile('[^a-zA-Z $]')
    return regex.sub('', text)


def count_words_from_file(filename):
    word_counts = defaultdict(int)
    with open(filename) as f:
        raw_words = remove_non_alpha_characters(f.read()).lower().split()
        for word in raw_words:
            word_counts[word] += 1
        return word_counts


if __name__ == '__main__':
    # TIP: remember about defaultdict in count_words: https://stackoverflow.com/a/5900628/1565454
    assert "there will be code".split() == ['there', 'will', 'be', 'code']
    assert "there-will-be-code".split('-') == ['there', 'will', 'be', 'code']

    small_dict = {
        'Alice': 1,
    }
    assert 'Alice' in small_dict
    assert 'Bob' not in small_dict
    small_dict['Bob'] = 0
    assert small_dict['Bob'] == 0

    # Exercise 1: make it pass
    easy_counts = count_words_from_file('./data/easy_text.txt')
    assert easy_counts == {'a': 2, 'small': 1, 'text': 1, 'with': 1, 'few': 1, 'repetitions': 1}

    # Exercise 2: make it pass
    assert remove_non_alpha_characters('Remove non alpha!') == 'Remove non alpha'
    assert 'Capitalized'.lower() == 'capitalized'
    alice_words = count_words_from_file('./data/regular_text.txt')
    assert alice_words['was'] == 3
    assert alice_words['of'] == 5
    assert 'Alice' not in alice_words
    assert alice_words['alice'] == 2
