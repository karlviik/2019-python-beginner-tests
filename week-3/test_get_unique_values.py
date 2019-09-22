import random
import string

import pytest
import exam

# input dict
# output list of unique dictionary values, order not important


@pytest.mark.timeout(1.0)
def test_get_unique_values_01():
    # all unique
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({1: 1, 2: 2, 3: 3}), {1, 2, 3})
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({1: "a", "d": "b", 3.2: "c"}), {"a", "b", "c"})


@pytest.mark.timeout(1.0)
def test_get_unique_values_02():
    # non unique
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({1: 1, 2: 1, 3: 1}), {1})
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({1: "a", 2: "a", 3: "a"}), {"a"})


@pytest.mark.timeout(1.0)
def test_get_unique_values_03():
    # various
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({1: 1 + 2j, 2: 1, 3: 2}), {1 + 2j, 1, 2})
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({1: -1, 1182: -1, -100: -1}), {-1})


@pytest.mark.timeout(1.0)
def test_get_unique_values_04():
    # empty dict
    assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values({}), set())


@pytest.mark.timeout(5.0)
def test_get_unique_values_05():
    # random
    for _ in range(100):
        dictionary = {}
        for i in range(100):
            dictionary[i] = "".join(random.choices(string.ascii_letters, k=random.randint(1, 3)))
        solution = set([x for x in dictionary.values()])
        assert (lambda x, y: len(x) == len(y) and set(x) == y)(exam.get_unique_values(dictionary), solution)
