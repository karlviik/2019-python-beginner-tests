import random
import string

import pytest
import exam

# input string
# output dict where key is symbol and value is number of times symbol appeared in string


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_01():
    # no repeats
    assert exam.count_symbol_appearances("abc") == {"a": 1, "b": 1, "c": 1}
    assert exam.count_symbol_appearances("a b_c") == {"a": 1, "b": 1, "c": 1, " ": 1, "_": 1}


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_02():
    # repeats
    assert exam.count_symbol_appearances("abba") == {"a": 2, "b": 2}
    assert exam.count_symbol_appearances("     .     ") == {" ": 10, ".": 1}


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_03():
    # same letter diff size
    assert exam.count_symbol_appearances("aAbB") == {"a": 1, "A": 1, "b": 1, "B": 1}


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_04():
    # empty string
    assert exam.count_symbol_appearances("") == {}


@pytest.mark.timeout(5.0)
def test_count_symbol_appearances_05():
    # random
    for _ in range(100):
        stringy_string = "".join(random.choices(string.ascii_letters, k=random.randint(0, 100)))
        solution = {}
        for symbol in stringy_string:
            solution.setdefault(symbol, 0)
            solution[symbol] += 1
        assert exam.count_symbol_appearances(stringy_string) == solution
