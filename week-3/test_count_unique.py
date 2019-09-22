import random

import pytest
import exam


# input list of numbers (any type)
# output number of unique numbers in list


@pytest.mark.timeout(1.0)
def test_count_unique_01():
    # no repeats
    assert exam.count_unique([1]) == 1
    assert exam.count_unique([1, 2, 3, 4]) == 4
    assert exam.count_unique([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11


@pytest.mark.timeout(1.0)
def test_count_unique_02():
    # with repeats
    assert exam.count_unique([1, 1, 2, 3, 3, 4]) == 4
    assert exam.count_unique([1, 1, 1, 1, 1, 1]) == 1
    assert exam.count_unique([1, 2, 3, 1, 2, 3, 3, 2, 1, 2]) == 3


@pytest.mark.timeout(1.0)
def test_count_unique_03():
    # empty list
    assert exam.count_unique([]) == 0


@pytest.mark.timeout(1.0)
def test_count_unique_04():
    # different datatype numbers
    assert exam.count_unique([1, 1.0, 1.000]) == 1
    assert exam.count_unique([1, 1.2, 1.5, 2]) == 4
    assert exam.count_unique([1, 2 + 3j, 4.1]) == 3


@pytest.mark.timeout(5.0)
def test_count_unique_05():
    # random
    for _ in range(100):
        numbers = []
        for _ in range(random.randint(0, 100)):
            chance = random.randint(0, 2)
            if chance == 0:
                numbers.append(random.randint(0, 10))
            if chance == 1:
                numbers.append(round(random.uniform(0, 10), 1))
            if chance == 2:
                numbers.append((1 + 1j + random.randint(-5, 5)) * random.randint(-5, 5))
        assert exam.count_unique(numbers) == len(set(numbers))

