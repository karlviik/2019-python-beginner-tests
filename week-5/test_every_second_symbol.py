import random
import string

import pytest
import exam

# sõne. tagastada sõne, kus on algse sõne iga teine sümbol: "tere" => "tr"
# "abcdef" => "ace"


@pytest.mark.timeout(1.0)
def test_every_second_symbol_01():
    # less than 3 symbols
    assert exam.every_second_symbol("a") == "a"
    assert exam.every_second_symbol("ab") == "a"


@pytest.mark.timeout(1.0)
def test_every_second_symbol_02():
    # exact symbol amount
    assert exam.every_second_symbol("abcde") == "ace"
    assert exam.every_second_symbol("1232231") == "1321"


@pytest.mark.timeout(1.0)
def test_every_second_symbol_03():
    # nonexact symbol count
    assert exam.every_second_symbol("abcd") == "ac"
    assert exam.every_second_symbol(" 1 2 3") == "   "


@pytest.mark.timeout(1.0)
def test_every_second_symbol_04():
    # empty string
    assert exam.every_second_symbol("") == ""


@pytest.mark.timeout(5.0)
def test_every_second_symbol_05():
    # random
    for _ in range(100):
        stringy = "".join(random.choices(string.ascii_letters, k=random.randint(0, 50)))
        assert exam.every_second_symbol(stringy) == stringy[::2]
