import random
import string

import pytest
import exam

# antakse list sõnedest. liida kokku sõned pikkusega 1, nt: ["a", "bb", "", "c"] => "ac"


@pytest.mark.timeout(1.0)
def test_join_symbols_01():
    # no symbols
    assert exam.join_symbols(["", "abc", "ccd"]) == ""
    assert exam.join_symbols(["ab", "ab", "ab"]) == ""


@pytest.mark.timeout(1.0)
def test_join_symbols_02():
    # all symbols
    assert exam.join_symbols(["a", "b", "c"]) == "abc"
    assert exam.join_symbols(["a", ",", " "]) == "a, "


@pytest.mark.timeout(1.0)
def test_join_symbols_03():
    # some symbols
    assert exam.join_symbols(["h", "e ", " y", "y"]) == "hy"
    assert exam.join_symbols([" ", "  ", " ", "    "]) == "  "


@pytest.mark.timeout(1.0)
def test_join_symbols_04():
    # empty list
    assert exam.join_symbols([]) == ""


@pytest.mark.timeout(5.0)
def test_join_symbols_05():
    # random
    for _ in range(100):
        str_list = ["".join(random.choices(string.ascii_letters, k=random.randint(0, 3))) for _ in range(random.randint(0, 25))]
        assert exam.join_symbols(str_list) == "".join([x for x in str_list if len(x) == 1])
