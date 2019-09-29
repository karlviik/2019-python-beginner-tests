import random

import pytest
import exam

# antakse minutite arv (0 <= z < 1440). tagastada ennik tund, minut:
# 10 => 0, 10
# 100 => 1, 40
# 1000 => 16, 40


@pytest.mark.timeout(1.0)
def test_minutes_to_hours_and_minutes_tuple_01():
    # less than hour
    assert exam.minutes_to_hours_and_minutes_tuple(10) == (0, 10)
    assert exam.minutes_to_hours_and_minutes_tuple(59) == (0, 59)


@pytest.mark.timeout(1.0)
def test_minutes_to_hours_and_minutes_tuple_02():
    # exact hours
    assert exam.minutes_to_hours_and_minutes_tuple(60) == (1, 0)
    assert exam.minutes_to_hours_and_minutes_tuple(240) == (4, 0)


@pytest.mark.timeout(1.0)
def test_minutes_to_hours_and_minutes_tuple_03():
    # hours and minutes
    assert exam.minutes_to_hours_and_minutes_tuple(321) == (5, 21)
    assert exam.minutes_to_hours_and_minutes_tuple(123) == (2, 3)


@pytest.mark.timeout(1.0)
def test_minutes_to_hours_and_minutes_tuple_04():
    # zero
    assert exam.minutes_to_hours_and_minutes_tuple(0) == (0, 0)


@pytest.mark.timeout(5.0)
def test_minutes_to_hours_and_minutes_tuple_05():
    # random
    for _ in range(100):
        minutes = random.randint(0, 1439)
        assert exam.minutes_to_hours_and_minutes_tuple(minutes) == (minutes // 60, minutes - 60 * (minutes // 60))
