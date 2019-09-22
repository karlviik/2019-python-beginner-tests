import random

import exam
import pytest


# input list of ints, can be empty list
# return min int, if list is empty return None


@pytest.mark.timeout(1.0)
def test_return_min_01():
    # positive min
    assert exam.return_min([1, 2, 3]) == 1
    assert exam.return_min([0, 1, 2]) == 0
    assert exam.return_min([0]) == 0


@pytest.mark.timeout(1.0)
def test_return_min_02():
    # negative min
    assert exam.return_min([1, 0, -1, -2, -3]) == -3
    assert exam.return_min([0, -10, -20, -500]) == -500


@pytest.mark.timeout(1.0)
def test_return_min_03():
    # all is same
    assert exam.return_min([1, 1, 1, 1, 1, 1]) == 1
    assert exam.return_min([-12, -12, -12, -12, -12]) == -12
    assert exam.return_min([0, 0, 0, 0, 0, 0]) == 0


@pytest.mark.timeout(1.0)
def test_return_min_04():
    # empty list
    assert exam.return_min([]) is None


@pytest.mark.timeout(5.0)
def test_return_min_05():
    # random
    for _ in range(100):
        numbers = [random.randint(-100, 100) for _ in range(random.randint(0, 25))]
        print(numbers)
        assert exam.return_min(numbers) == (min(numbers) if len(numbers) > 0 else None)
