import random
import string

import pytest
import exam

# input string with symbols
# return list of numbers as ints in the string in the order they appeared in


@pytest.mark.timeout(1.0)
def test_numbers_in_string_01():
    # no numbers
    assert exam.numbers_in_string("qwerty") == []
    assert exam.numbers_in_string("o/") == []


@pytest.mark.timeout(1.0)
def test_numbers_in_string_02():
    # some numbers
    assert exam.numbers_in_string("a1karamba") == [1]
    assert exam.numbers_in_string("fb23gs3g1") == [2, 3, 3, 1]
    assert exam.numbers_in_string("1k6jd93hsa") == [1, 6, 9, 3]


@pytest.mark.timeout(1.0)
def test_numbers_in_string_03():
    # all numbers
    assert exam.numbers_in_string("12321") == [1, 2, 3, 2, 1]
    assert exam.numbers_in_string("000") == [0, 0, 0]


@pytest.mark.timeout(1.0)
def test_numbers_in_string_04():
    # empty string
    assert exam.numbers_in_string("") == []


@pytest.mark.timeout(5.0)
def test_numbers_in_string_05():
    # random
    for _ in range(100):
        stringy = "".join(random.choices([str(i) for i in list(range(0, 10))] + list(string.ascii_lowercase),
                                         k=random.randint(0, 50)))
        int_list = []
        for symbol in stringy:
            if symbol.isnumeric():
                int_list.append(int(symbol))
        assert exam.numbers_in_string(stringy) == int_list
