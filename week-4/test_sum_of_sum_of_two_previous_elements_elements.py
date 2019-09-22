import random

import pytest
import exam

# input list of ints
# return sum on those ints which are equal to sum of 2 previous elements


@pytest.mark.timeout(1.0)
def test_sum_of_sum_of_two_previous_elements_elements_01():
    # just one number, simple
    assert exam.sum_of_sum_of_two_previous_elements_elements([1, 2, 3]) == 3
    assert exam.sum_of_sum_of_two_previous_elements_elements([1, 1, 1, 1, 2, 2, 2, 2]) == 2


@pytest.mark.timeout(1.0)
def test_sum_of_sum_of_two_previous_elements_elements_02():
    # multiple numbers and negatives
    assert exam.sum_of_sum_of_two_previous_elements_elements([10, 10, 20, 0, 0, 1, 1]) == 21
    assert exam.sum_of_sum_of_two_previous_elements_elements([1, 2, 3, 5, 8]) == 16
    assert exam.sum_of_sum_of_two_previous_elements_elements([-1, -2, -3, 3, 0]) == -3


@pytest.mark.timeout(1.0)
def test_sum_of_sum_of_two_previous_elements_elements_03():
    # no numbers
    assert exam.sum_of_sum_of_two_previous_elements_elements([9, 7, 5, 3, 1]) == 0
    assert exam.sum_of_sum_of_two_previous_elements_elements([1, 4, 6, 9, 14]) == 0


@pytest.mark.timeout(1.0)
def test_sum_of_sum_of_two_previous_elements_elements_04():
    # too few numbers
    assert exam.sum_of_sum_of_two_previous_elements_elements([1, 2]) == 0
    assert exam.sum_of_sum_of_two_previous_elements_elements([1]) == 0
    assert exam.sum_of_sum_of_two_previous_elements_elements([]) == 0


@pytest.mark.timeout(5.0)
def test_sum_of_sum_of_two_previous_elements_elements_05():
    # random
    for _ in range(100):
        int_list = list(random.choices(list(range(-10, 10)), k=random.randint(0, 250)))
        int_sum = 0
        for i in range(2, len(int_list)):
            if int_list[i - 2] + int_list[i - 1] == int_list[i]:
                int_sum += int_list[i]
        assert exam.sum_of_sum_of_two_previous_elements_elements(int_list) == int_sum
