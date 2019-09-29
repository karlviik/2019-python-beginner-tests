import random

import pytest
import exam

# arvude list. tagastada list, kus on järjestikuste arvude vahe: [1, 4, 3] => [3, 1] . abs() vahe.
# [1] => []
# [1, 10, 10] => [9, 0]


@pytest.mark.timeout(1.0)
def test_difference_01():
    # too short
    assert exam.difference([]) == []
    assert exam.difference([1]) == []


@pytest.mark.timeout(1.0)
def test_difference_02():
    # one difference
    assert exam.difference([1, 2]) == [1]
    assert exam.difference([0, 10]) == [10]
    assert exam.difference([10, 0]) == [10]


@pytest.mark.timeout(1.0)
def test_difference_03():
    # multiple differences
    assert exam.difference([1, 2, 3, 2, 1]) == [1, 1, 1, 1]
    assert exam.difference([1, 4, 7, 4, 1, 1]) == [3, 3, 3, 3, 0]


@pytest.mark.timeout(1.0)
def test_difference_04():
    # negative numbers
    assert exam.difference([-1, 1, -1, 1, -1]) == [2, 2, 2, 2]
    assert exam.difference([-100, -10, 100, -1]) == [90, 110, 101]


@pytest.mark.timeout(5.0)
def test_difference_05():
    # random
    for _ in range(100):
        int_list = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        assert exam.difference(int_list) == [abs(int_list[x] - int_list[x + 1]) for x in range(len(int_list) - 1)]
