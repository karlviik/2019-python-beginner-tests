import random

import pytest
import exam

# input a subtraction and addition thing, can be empty string in which case result is 0
# return result


@pytest.mark.timeout(1.0)
def test_addition_and_subtraction_01():
    # easy addition and subtraction
    assert exam.addition_and_subtraction("1+2") == 3
    assert exam.addition_and_subtraction("1-2") == -1


@pytest.mark.timeout(1.0)
def test_addition_and_subtraction_02():
    # longer ones
    assert exam.addition_and_subtraction("1+2+3-5") == 1
    assert exam.addition_and_subtraction("8+9+10-9-8-10") == 0


@pytest.mark.timeout(1.0)
def test_addition_and_subtraction_03():
    # start with symbol
    assert exam.addition_and_subtraction("-1+8") == 7
    assert exam.addition_and_subtraction("+1+2+3") == 6


@pytest.mark.timeout(1.0)
def test_addition_and_subtraction_04():
    # empty string or just a number
    assert exam.addition_and_subtraction("") == 0
    assert exam.addition_and_subtraction("1") == 1
    assert exam.addition_and_subtraction("-1") == -1


@pytest.mark.timeout(5.0)
def test_addition_and_subtraction_05():
    # random
    for _ in range(100):
        stringy = "".join([str(random.randint(0, 100)) + "".join(random.choices("+-", k=1)) for _ in range(0, 25)]
                          + [str(random.randint(0, 100))])
        result = 0
        current_number = "0"
        for symbol in stringy:
            if not symbol.isnumeric():
                result += int(current_number)
                current_number = ""
            current_number += symbol
        assert exam.addition_and_subtraction(stringy) == result + int(current_number)
