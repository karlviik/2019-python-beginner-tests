import random
import string

import pytest
import exam

# input two sets
# output if one set contains whole other set


@pytest.mark.timeout(1.0)
def test_compare_sets_01():
    # simple trues
    assert exam.compare_sets({1}, {1, 2, 3}) is True
    assert exam.compare_sets({1, 2, 3}, {1}) is True
    assert exam.compare_sets({"a", 1, 2.2}, {2.2}) is True


@pytest.mark.timeout(1.0)
def test_compare_sets_02():
    # simple falses
    assert exam.compare_sets({1, 2}, {"1", "2"}) is False
    assert exam.compare_sets({1, 2}, {2, 3}) is False
    assert exam.compare_sets({1}, {1.1}) is False


@pytest.mark.timeout(1.0)
def test_compare_sets_03():
    # same sets
    assert exam.compare_sets({1, 2, 3}, {1, 2, 3}) is True
    assert exam.compare_sets({"a", 1, 1 + 1j}, {"a", 1, 1 + 1j}) is True


@pytest.mark.timeout(1.0)
def test_compare_sets_04():
    # empty sets
    assert exam.compare_sets(set(), {1, 2}) is True
    assert exam.compare_sets({1, 2}, set()) is True
    assert exam.compare_sets(set(), set()) is True


@pytest.mark.timeout(5.0)
def test_compare_sets_05():
    # random
    for _ in range(100):
        set_1 = set(random.choices(list(string.ascii_letters) + list(range(0, 100)), k=random.randint(0, 100)))
        set_2 = set(random.choices(list(set_1), k=random.randint(0, len(set_1))))
        if random.random() < 0.5:
            set_2.add(random.random())
        assert exam.compare_sets(set_1, set_2) == (set_1.difference(set_2) == set() or set_2.difference(set_1) == set())
        assert exam.compare_sets(set_2, set_1) == (set_1.difference(set_2) == set() or set_2.difference(set_1) == set())
