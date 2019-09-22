import random
import string

import pytest
import exam

# input string
# return number of symbols that overlap with same string but reversed


@pytest.mark.timeout(1.0)
def test_reverse_string_overlap_symbols_01():
    # no overlaps
    assert exam.reverse_string_overlap_symbols("abcd") == 0
    assert exam.reverse_string_overlap_symbols("abab") == 0


@pytest.mark.timeout(1.0)
def test_reverse_string_overlap_symbols_02():
    # some overlaps
    assert exam.reverse_string_overlap_symbols("abcda") == 3
    assert exam.reverse_string_overlap_symbols("abcdbc") == 2
    assert exam.reverse_string_overlap_symbols("aa") == 2


@pytest.mark.timeout(1.0)
def test_reverse_string_overlap_symbols_03():
    # palindrome
    assert exam.reverse_string_overlap_symbols("abcdcba") == 7
    assert exam.reverse_string_overlap_symbols("123321") == 6


@pytest.mark.timeout(1.0)
def test_reverse_string_overlap_symbols_04():
    # empty string
    assert exam.reverse_string_overlap_symbols("") == 0


@pytest.mark.timeout(5.0)
def test_reverse_string_overlap_symbols_05():
    # random
    for _ in range(200):
        stringy = "".join(random.choices(string.ascii_lowercase, k=random.randint(0, 50)))
        count = 0
        for i in range(0, len(stringy)):
            if stringy[i] == stringy[-1 - i]:
                count += 1
        assert exam.reverse_string_overlap_symbols(stringy) == count
