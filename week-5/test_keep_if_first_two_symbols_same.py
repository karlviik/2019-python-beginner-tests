import random
import string

import pytest
import exam

# järjendis sõned. jätta alles sõned, kus kaks esimest sümbolit on samad nt ["a", "bb", "bbs"] => ["bb", "bbs"]


@pytest.mark.timeout(1.0)
def test_keep_if_first_two_symbols_same_01():
    # too short strings
    assert exam.keep_if_first_two_symbols_same(["a"]) == []
    assert exam.keep_if_first_two_symbols_same(["a", "b", "b", "b"]) == []


@pytest.mark.timeout(1.0)
def test_keep_if_first_two_symbols_same_02():
    # no correct strings
    assert exam.keep_if_first_two_symbols_same(["abd", "aba", "abs", "ac", "ac"]) == []
    assert exam.keep_if_first_two_symbols_same(["abc", "abc", "abc", "abc"]) == []


@pytest.mark.timeout(1.0)
def test_keep_if_first_two_symbols_same_03():
    # all correct strings
    assert exam.keep_if_first_two_symbols_same(["aaa", "aa", "aaaa"]) == ["aaa", "aa", "aaaa"]
    assert exam.keep_if_first_two_symbols_same(["aab", "bba", "ccd", "hhi"]) == ["aab", "bba", "ccd", "hhi"]


@pytest.mark.timeout(1.0)
def test_keep_if_first_two_symbols_same_04():
    # empty list or empty string
    assert exam.keep_if_first_two_symbols_same([]) == []
    assert exam.keep_if_first_two_symbols_same([""]) == []


@pytest.mark.timeout(5.0)
def test_keep_if_first_two_symbols_same_05():
    # random
    for _ in range(100):
        str_list = ["".join(random.choices(string.ascii_lowercase[:5], k=random.randint(0, 5)))
                    for _ in range(random.randint(0, 100))]
        assert exam.keep_if_first_two_symbols_same(str_list) == [x for x in str_list if len(x) > 1 and x[0] == x[1]]
