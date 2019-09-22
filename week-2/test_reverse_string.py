import random
import string

import exam
import pytest


# input string of any length
# output reversed string


@pytest.mark.timeout(1.0)
def test_reverse_string_01():
    # simple string
    assert exam.reverse_string("a") == "a"
    assert exam.reverse_string("abc") == "cba"
    assert exam.reverse_string("AbCd") == "dCbA"
    assert exam.reverse_string(".b.a.c.h.") == ".h.c.a.b."


@pytest.mark.timeout(1.0)
def test_reverse_string_02():
    # palindrome
    assert exam.reverse_string("ABBA") == "ABBA"
    assert exam.reverse_string("tattarrattat") == "tattarrattat"


@pytest.mark.timeout(1.0)
def test_reverse_string_03():
    # empty string
    assert exam.reverse_string("") == ""


@pytest.mark.timeout(1.0)
def test_reverse_string_04():
    # whitespace
    assert exam.reverse_string(" heya") == "ayeh "
    assert exam.reverse_string("   woof    ") == "    foow   "
    assert exam.reverse_string("   ") == "   "


@pytest.mark.timeout(5.0)
def test_reverse_string_05():
    # random
    for _ in range(100):
        word = "".join(random.choices(string.printable, k=random.randint(0, 100)))
        assert exam.reverse_string(word) == word[::-1]
