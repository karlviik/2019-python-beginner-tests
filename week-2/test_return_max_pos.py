import random

import exam
import pytest


# input list of ints, can be empty in which case return -1
# return max pos, if multiple return leftmost


@pytest.mark.timeout(1.0)
def test_return_max_pos_01():
    # positive max pos
    assert exam.return_max_pos([1, 2, 3]) == 2
    assert exam.return_max_pos([0, 1, 0]) == 1
    assert exam.return_max_pos([0]) == 0


@pytest.mark.timeout(1.0)
def test_return_max_pos_02():
    # negative max pos
    assert exam.return_max_pos([-1, -2, -3]) == 0
    assert exam.return_max_pos([-50, -10, -20, -500]) == 1


@pytest.mark.timeout(1.0)
def test_return_max_pos_03():
    # multiple max
    assert exam.return_max_pos([1, 1, 1, 1]) == 0
    assert exam.return_max_pos([-12, -11, -12, -11]) == 1
    assert exam.return_max_pos([1, 2, 3, 3, 2, 1, 3, 3, 3]) == 2


@pytest.mark.timeout(1.0)
def test_return_max_pos_04():
    # empty list
    assert exam.return_max_pos([]) == -1


@pytest.mark.timeout(5.0)
def test_return_max_pos_05():
    # random
    for _ in range(100):
        numbers = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        assert exam.return_max_pos(numbers) == numbers.index(max(numbers)) if len(numbers) > 0 \
            else exam.return_max_pos(numbers) == -1
