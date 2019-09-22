import random
import string

import pytest
import exam

# input string with numbers and characters
# return int that's built from numbers in that string in the order they appeared in. If no numbers, 0


@pytest.mark.timeout(1.0)
def test_number_from_string_01():
    # no number
    assert exam.number_from_string("abcd") == 0
    assert exam.number_from_string("a") == 0


@pytest.mark.timeout(1.0)
def test_number_from_string_02():
    # few numbers
    assert exam.number_from_string("a6b7c8d9") == 6789
    assert exam.number_from_string("1abc12def34") == 11234


@pytest.mark.timeout(1.0)
def test_number_from_string_03():
    # all numbers
    assert exam.number_from_string("12345") == 12345
    assert exam.number_from_string("0123") == 123


@pytest.mark.timeout(1.0)
def test_number_from_string_04():
    # empty string
    assert exam.number_from_string("") == 0


@pytest.mark.timeout(5.0)
def test_number_from_string_05():
    # random
    for _ in range(100):
        stringy = "".join(random.choices([str(i) for i in list(range(0, 10))] + list(string.ascii_lowercase),
                                         k=random.randint(0, 50)))
        assert exam.number_from_string(stringy) == int("".join([i for i in "0" + stringy if i.isnumeric()]))
