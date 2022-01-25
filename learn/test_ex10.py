phrase = input("Set a phrase: ")
phrase_len = len(phrase)


def test_length():
    assert phrase_len < 15, f'length phrase is more than 15 symbols '
