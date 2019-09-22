import random
import string

import pytest
import exam

# input list of strings
# output dict where key is symbol and value is list of strings that start with that symbol


@pytest.mark.timeout(1.0)
def test_organise_by_first_symbol_01():
    # different start words
    assert exam.organise_by_first_symbol(["abc", "def", "ghi"]) == {"a": ["abc"], "d": ["def"], "g": ["ghi"]}
    assert exam.organise_by_first_symbol(["a", "b", "c"]) == {"a": ["a"], "b": ["b"], "c": ["c"]}


@pytest.mark.timeout(1.0)
def test_organise_by_first_symbol_02():
    # same start words
    assert exam.organise_by_first_symbol(["ab", "ac", "ad"]) == {"a": ["ab", "ac", "ad"]}
    assert exam.organise_by_first_symbol(["ab", "cd", "ab"]) == {"a": ["ab", "ab"], "c": ["cd"]}


@pytest.mark.timeout(1.0)
def test_organise_by_first_symbol_03():
    # exotic start symbols
    assert exam.organise_by_first_symbol([" a", " b", "%a"]) == {" ": [" a", " b"], "%": ["%a"]}
    assert exam.organise_by_first_symbol(["!a", "?a", "!d"]) == {"!": ["!a", "!d"], "?": ["?a"]}


@pytest.mark.timeout(1.0)
def test_organise_by_first_symbol_04():
    # empty list
    assert exam.organise_by_first_symbol([]) == {}


@pytest.mark.timeout(5.0)
def test_organise_by_first_symbol_05():
    # random
    for _ in range(100):
        strings = ["".join(random.choices(string.ascii_letters, k=random.randint(1, 10))) for _ in range(50)]
        solution = {}
        for word in strings:
            solution.setdefault(word[0], [])
            solution[word[0]] += [word]
        assert exam.organise_by_first_symbol(strings) == solution
