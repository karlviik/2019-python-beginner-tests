import random
import string

import exam
import pytest


# input a string of ascii letter words, separated with 1 space, no spaces in beginning or end, no special characters
# output string where each word's first letter is capitalised, rest is same


@pytest.mark.timeout(1.0)
def test_capitalise_words_01():
    # 1 word simple
    assert exam.capitalise_words("a") == "A"
    assert exam.capitalise_words("A") == "A"
    assert exam.capitalise_words("abc") == "Abc"
    assert exam.capitalise_words("Abc") == "Abc"


@pytest.mark.timeout(1.0)
def test_capitalise_words_02():
    # 2 or more words simple
    assert exam.capitalise_words("a B") == "A B"
    assert exam.capitalise_words("abc Def") == "Abc Def"


@pytest.mark.timeout(1.0)
def test_capitalise_words_03():
    # empty string
    assert exam.capitalise_words("") == ""


@pytest.mark.timeout(1.0)
def test_capitalise_words_04():
    # ignore caps letters
    assert exam.capitalise_words("aBc") == "ABc"
    assert exam.capitalise_words("ABC DEF GHI") == "ABC DEF GHI"


@pytest.mark.timeout(5.0)
def test_capitalise_words_05():
    # random
    for _ in range(100):
        sentence = " ".join("".join(random.choices(string.ascii_letters, k=random.randint(1, 10)))
                            for _ in range(random.randint(0, 100)))
        assert exam.capitalise_words(sentence) == " ".join(k[0].capitalize() + k[1:] for k in sentence.split())
