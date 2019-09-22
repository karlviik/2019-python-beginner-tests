import random

import exam
import pytest


# input row count, >= 0
# return rows with +1 increasing asterisk count, starting from 1 on row 1

@pytest.mark.timeout(1.0)
def test_starry_night_01():
    # test 1
    assert exam.starry_night(1) == "*"


@pytest.mark.timeout(1.0)
def test_starry_night_02():
    # test 2
    assert exam.starry_night(2) == "*\n**"


@pytest.mark.timeout(1.0)
def test_starry_night_03():
    # test 0
    assert exam.starry_night(0) == ""


@pytest.mark.timeout(1.0)
def test_starry_night_04():
    # test 6
    assert exam.starry_night(6) == "*\n**\n***\n****\n*****\n******"


@pytest.mark.timeout(5.0)
def test_starry_night_05():
    # random
    for _ in range(100):
        rows = random.randint(0, 1000)
        assert exam.starry_night(rows) == "\n".join("*" * x for x in range(1, rows + 1))
