import random

import pytest
import exam

# ristsumma. antakse täisarv, tuleb leida ristsumma 12 => 3, 12345 => 15


@pytest.mark.timeout(1.0)
def test_cross_sum_01():
    # short numbers
    assert exam.cross_sum(5) == 5
    assert exam.cross_sum(12) == 3


@pytest.mark.timeout(1.0)
def test_cross_sum_02():
    # longer numbers
    assert exam.cross_sum(12345) == 15
    assert exam.cross_sum(1111111111) == 10


@pytest.mark.timeout(1.0)
def test_cross_sum_03():
    # negative numbers
    assert exam.cross_sum(-10) == 1
    assert exam.cross_sum(-123) == 6


@pytest.mark.timeout(1.0)
def test_cross_sum_04():
    # zero
    assert exam.cross_sum(0) == 0


@pytest.mark.timeout(5.0)
def test_cross_sum_05():
    # random
    for _ in range(100):
        integer = random.randint(-100000, 100000)
        assert exam.cross_sum(integer) == sum([int(x) for x in str(abs(integer))])
