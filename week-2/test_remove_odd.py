import random

import exam
import pytest


# input list of ints
# return list without odds, keep the order


@pytest.mark.timeout(1.0)
def test_remove_odd_01():
    # remove one
    assert exam.remove_odd([1, 2, 4]) == [2, 4]
    assert exam.remove_odd([2, 1, 4]) == [2, 4]
    assert exam.remove_odd([4, 2, 1]) == [4, 2]


@pytest.mark.timeout(1.0)
def test_remove_odd_02():
    # more complex
    assert exam.remove_odd([1, 2, 3, 4, 5]) == [2, 4]
    assert exam.remove_odd([1, 1, 1, 2, 1, 1]) == [2]
    assert exam.remove_odd([0, 2, 4]) == [0, 2, 4]


@pytest.mark.timeout(1.0)
def test_remove_odd_03():
    # negative
    assert exam.remove_odd([-1, 0, 1]) == [0]
    assert exam.remove_odd([-3, -5, -7, 8, 6, 4, 6]) == [8, 6, 4, 6]


@pytest.mark.timeout(1.0)
def test_remove_odd_04():
    # remove to empty list
    assert exam.remove_odd([1, 3, 5]) == []
    assert exam.remove_odd([-1, -3, -5]) == []
    assert exam.remove_odd([]) == []


@pytest.mark.timeout(5.0)
def test_remove_odd_05():
    # random
    for _ in range(100):
        numbers = [random.randint(-100, 100) for _ in range(random.randint(0, 25))]
        assert exam.remove_odd(numbers) == [x for x in numbers if x % 2 == 0]
