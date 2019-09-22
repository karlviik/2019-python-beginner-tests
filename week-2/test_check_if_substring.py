import random
import string

import exam
import pytest


# input 2 strings with length of at least 1
# case sensitive
# output boolean


@pytest.mark.timeout(1.0)
def test_check_if_substring_01():
    # 1 contains 2
    assert exam.check_if_substring("a", "abc") is True
    assert exam.check_if_substring("Bc", "aBc ") is True
    assert exam.check_if_substring("c .?", "aBc .?") is True


@pytest.mark.timeout(1.0)
def test_check_if_substring_02():
    # 2 contains 1
    assert exam.check_if_substring("aBc", "a") is True
    assert exam.check_if_substring("aBc ", "Bc") is True
    assert exam.check_if_substring("aBc .?", "c .?") is True


@pytest.mark.timeout(1.0)
def test_check_if_substring_03():
    # no match
    assert exam.check_if_substring("a", "b") is False
    assert exam.check_if_substring("ABC", "abc") is False
    assert exam.check_if_substring("bC=)2", "C=)23") is False
    assert exam.check_if_substring(" a b c", "a b c ") is False


@pytest.mark.timeout(1.0)
def test_check_if_substring_04():
    # 1 is 2
    assert exam.check_if_substring("a", "a") is True
    assert exam.check_if_substring("aB1!%", "aB1!%") is True
    assert exam.check_if_substring(" ", " ") is True


@pytest.mark.timeout(5.0)
def test_check_if_substring_05():
    # random
    for _ in range(100):
        big_string = "".join(random.choices(string.ascii_letters, k=random.randint(1, 100)))
        small_string_start = random.randint(0, len(big_string) - 1)
        small_string = big_string[small_string_start:random.randint(small_string_start + 1, len(big_string))]
        assert exam.check_if_substring(big_string, small_string) is True
        assert exam.check_if_substring(small_string, big_string) is True
        assert exam.check_if_substring(big_string, "!") is False
        assert exam.check_if_substring("!", small_string) is False
