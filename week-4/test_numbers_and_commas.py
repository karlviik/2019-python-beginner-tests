import random

import pytest
import exam

# input string with commas and numbers, like "1,2,3,34"
# return list of those numbers, like [1, 2, 3, 34]


@pytest.mark.timeout(1.0)
def test_numbers_and_commas_01():
    # just one number
    assert exam.numbers_and_commas("1") == [1]
    assert exam.numbers_and_commas("11") == [11]


@pytest.mark.timeout(1.0)
def test_numbers_and_commas_02():
    # few numbers
    assert exam.numbers_and_commas("1,2,3") == [1, 2, 3]
    assert exam.numbers_and_commas("1,22,333") == [1, 22, 333]


@pytest.mark.timeout(1.0)
def test_numbers_and_commas_03():
    # negative numbers
    assert exam.numbers_and_commas("1,-1,-10") == [1, -1, -10]
    assert exam.numbers_and_commas("-1,-2,-1") == [-1, -2, -1]


@pytest.mark.timeout(1.0)
def test_numbers_and_commas_04():
    # empty string or just comma or comma in beginning/end
    assert exam.numbers_and_commas("") == []
    assert exam.numbers_and_commas(",") == []
    assert exam.numbers_and_commas(",1,2,") == [1, 2]


@pytest.mark.timeout(5.0)
def test_numbers_and_commas_05():
    # random
    for _ in range(100):
        stringy = ",".join([str(random.randint(-100, 100)) for i in range(random.randint(1, 50))])
        assert exam.numbers_and_commas(stringy) == [int(i) for i in stringy.strip(",").split(",")] \
            if len(stringy.strip(",")) != 0 else []
