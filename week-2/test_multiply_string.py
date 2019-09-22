import random
import string

import exam
import pytest


# input a string of any length any characters and int from 0 or over
# output same string times the int from input


@pytest.mark.timeout(1.0)
def test_multiply_string_01():
    # easy
    assert exam.multiply_string("ab", 1) == "ab"
    assert exam.multiply_string("ab", 2) == "abab"
    assert exam.multiply_string("A", 3) == "AAA"


@pytest.mark.timeout(1.0)
def test_multiply_string_02():
    # diff chars
    assert exam.multiply_string("a b", 3) == "a ba ba b"
    assert exam.multiply_string("a ", 3) == "a a a "
    assert exam.multiply_string(" ab", 3) == " ab ab ab"
    assert exam.multiply_string("!2# aG ", 4) == "!2# aG !2# aG !2# aG !2# aG "


@pytest.mark.timeout(1.0)
def test_multiply_string_03():
    # empty string
    assert exam.multiply_string("", 1) == ""
    assert exam.multiply_string("", 3) == ""


@pytest.mark.timeout(1.0)
def test_multiply_string_04():
    # zero
    assert exam.multiply_string("a", 0) == ""
    assert exam.multiply_string("a b c d", 0) == ""
    assert exam.multiply_string("", 0) == ""


@pytest.mark.timeout(5.0)
def test_multiply_string_05():
    # random
    for _ in range(100):
        input_string = "".join(random.choices(string.printable, k=random.randint(1, 10)))
        multiplier = random.randint(0, 20)
        assert exam.multiply_string(input_string, multiplier) == input_string * multiplier
