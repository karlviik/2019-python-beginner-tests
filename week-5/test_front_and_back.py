import random

import pytest
import exam

# antud list intidest, võta kordamööda eest- ja tagantpoolt ja tagasta saadud list. nt: 1,2,3,4,5,6 => 1,6,2,5,3,4


@pytest.mark.timeout(1.0)
def test_front_and_back_01():
    # very short list
    assert exam.front_and_back([1]) == [1]
    assert exam.front_and_back([1, 2]) == [1, 2]


@pytest.mark.timeout(1.0)
def test_front_and_back_02():
    # longer even list
    assert exam.front_and_back([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
    assert exam.front_and_back([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 8, 2, 7, 3, 6, 4, 5]


@pytest.mark.timeout(1.0)
def test_front_and_back_03():
    # longer odd list
    assert exam.front_and_back([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert exam.front_and_back([1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4]


@pytest.mark.timeout(1.0)
def test_front_and_back_04():
    # empty list
    assert exam.front_and_back([]) == []


@pytest.mark.timeout(5.0)
def test_front_and_back_05():
    # random
    for _ in range(100):
        int_list = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        assert exam.front_and_back(int_list) == [int_list[(z + 1) // 2 * (-1) ** z] for z in range(len(int_list))]
