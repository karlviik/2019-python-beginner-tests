import random
import string

import pytest
import exam

# input list of strings
# return longest string, if multiple then first, if none exist then None


@pytest.mark.timeout(1.0)
def test_longest_string_01():
    # just one string
    assert exam.longest_string(["hello"]) == "hello"
    assert exam.longest_string([" . "]) == " . "


@pytest.mark.timeout(1.0)
def test_longest_string_02():
    # multiple strings
    assert exam.longest_string(["would", "you", "like", "fries", "with", "that"]) == "would"
    assert exam.longest_string(["yes", "thank", "you", "I'd", "want", "all", "the", "fries", "you", "have"]) == "thank"


@pytest.mark.timeout(1.0)
def test_longest_string_03():
    # empty strings
    assert exam.longest_string([""]) == ""
    assert exam.longest_string(["", "", "", ""]) == ""


@pytest.mark.timeout(1.0)
def test_longest_string_04():
    # no strings
    assert exam.longest_string([]) is None


@pytest.mark.timeout(5.0)
def test_longest_string_05():
    # random
    for _ in range(100):
        str_list = ["".join(random.choices(string.ascii_letters, k=random.randint(0, 50)))
                    for i in range(0, random.randint(0, 25))]
        longest_str = None
        longest_length = -1
        for stringy in str_list:
            if len(stringy) > longest_length:
                longest_length = len(stringy)
                longest_str = stringy
        assert exam.longest_string(str_list) == longest_str
