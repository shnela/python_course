import re


def remove_non_alpha_characters(text):
    regex = re.compile('[^a-zA-Z $]')
    return regex.sub('', text)


def count_words(text):
    return dict()


if __name__ == '__main__':
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
    easy_text = 'a small text with a few repetitions'
    assert count_words(easy_text) == {'a': 2, 'small': 1, 'text': 1, 'with': 1, 'few': 1, 'repetitions': 1}

    # Exercise 2: make it pass
    assert remove_non_alpha_characters('Remove non alpha!') == 'Remove non alpha'
    assert 'Capitalized'.lower() == 'capitalized'
    regular_text = """ALICE was beginning to get very tired of sitting by her sister on the bank and of having nothing
to do: once or twice she had peeped into the book her sister was reading, but it had no pictures
or conversations in it, "and what is the use of a book," thought Alice, "without pictures or conversations?'
So she was considering, in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid),
whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies,
when suddenly a White Rabbit with pink eyes ran close by her."""
    alice_words = count_words(regular_text)
    assert alice_words['was'] == 3
    assert alice_words['of'] == 5
    assert 'Alice' not in alice_words
    assert alice_words['alice'] == 2

    # Exercise 3: use defaultdict in count_words: https://stackoverflow.com/a/5900628/1565454
