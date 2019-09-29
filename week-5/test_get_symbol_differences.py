import random
import string

import pytest
import exam


# sõne väikestest ladina tähtedest. kahe kõrvutioleva tähe vahe. "abc" => [1, 1]
# "ada" => [3, -1]
# "a" => []
# "akm" => [10, 2]


@pytest.mark.timeout(1.0)
def test_get_symbol_differences_01():
    # not enough symbols
    assert exam.get_symbol_differences("") == []
    assert exam.get_symbol_differences("a") == []


@pytest.mark.timeout(1.0)
def test_get_symbol_differences_02():
    # increasing differences
    assert exam.get_symbol_differences("abd") == [1, 2]
    assert exam.get_symbol_differences("acg") == [2, 4]


@pytest.mark.timeout(1.0)
def test_get_symbol_differences_03():
    # decreasing differences
    assert exam.get_symbol_differences("gfe") == [-1, -1]
    assert exam.get_symbol_differences("gca") == [-4, -2]


@pytest.mark.timeout(1.0)
def test_get_symbol_differences_04():
    # various differences
    assert exam.get_symbol_differences("abab") == [1, -1, 1]
    assert exam.get_symbol_differences("acea") == [2, 2, -4]


@pytest.mark.timeout(5.0)
def test_get_symbol_differences_05():
    # random
    for _ in range(100):
        stringy = "".join(random.choices(string.ascii_lowercase, k=random.randint(0, 50)))
        assert exam.get_symbol_differences(stringy) == [string.ascii_lowercase.find(stringy[x])
                                                        - string.ascii_lowercase.find(stringy[x - 1])
                                                        for x in range(1, len(stringy))]
