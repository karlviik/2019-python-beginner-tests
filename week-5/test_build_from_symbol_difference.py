import random
import string

import pytest
import exam


# eelmise pöördfunktsioon. antakse esimene täht ja list tähede vahest:
# "a", [1, 1] => "abc"
# "a", [] => "a"
# "a", [10, -2] => "aki"


@pytest.mark.timeout(1.0)
def test_build_from_symbol_difference_01():
    # no differences
    assert exam.build_from_symbol_difference("a", []) == "a"


@pytest.mark.timeout(1.0)
def test_build_from_symbol_difference_02():
    # increasing differences
    assert exam.build_from_symbol_difference("a", [1, 1, 1]) == "abcd"
    assert exam.build_from_symbol_difference("a", [1, 2, 3]) == "abdg"


@pytest.mark.timeout(1.0)
def test_build_from_symbol_difference_03():
    # decreasing differences
    assert exam.build_from_symbol_difference("k", [-1, -1]) == "kji"
    assert exam.build_from_symbol_difference("k", [-2, -4]) == "kie"


@pytest.mark.timeout(1.0)
def test_build_from_symbol_difference_04():
    # various differences
    assert exam.build_from_symbol_difference("a", [1, -1, 1]) == "abab"
    assert exam.build_from_symbol_difference("c", [-2, 2, 3, -5]) == "cacfa"


@pytest.mark.timeout(5.0)
def test_build_from_symbol_difference_05():
    # random
    for _ in range(100):
        stringy = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 50)))
        differences = [string.ascii_lowercase.find(stringy[x]) - string.ascii_lowercase.find(stringy[x - 1])
                       for x in range(1, len(stringy))]
        assert exam.build_from_symbol_difference(stringy[0], differences) == stringy
