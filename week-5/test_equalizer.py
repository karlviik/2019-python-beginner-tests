import random

import pytest
import exam

# arvude "tasandamine". järjend täisarvudest. arv, mis on kahe väiksema arvu vahel, tuleb vähendada.
# arv, mis asub kahe suurema arvu vahel, tuleb suurendada.
# neid täidetakse järjest (st vasakult rakendad seda reeglit järjest).
# [1, 4, 1] => [1, 3, 1]
# [1, 2] => [1, 2]
# [1, 4, 1, 0, 2] => [1, 3, 1, 1, 2]
# [1, 4, 1, 4, 1] => [1, 3, 2, 3, 1]
# [1, 2, 1, 2, 1] => [1, 1, 1, 1, 1]


@pytest.mark.timeout(1.0)
def test_equalizer_01():
    # too short to equalize
    assert exam.equalizer([]) == []
    assert exam.equalizer([1]) == [1]
    assert exam.equalizer([1, 2]) == [1, 2]


@pytest.mark.timeout(1.0)
def test_equalizer_02():
    # nothing to equalize
    assert exam.equalizer([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert exam.equalizer([1, 1, 1, 1]) == [1, 1, 1, 1]


@pytest.mark.timeout(1.0)
def test_equalizer_03():
    # equalizable but change affects it
    assert exam.equalizer([1, 2, 1, 2]) == [1, 1, 1, 2]
    assert exam.equalizer([2, 1, 2, 1]) == [2, 2, 2, 1]


@pytest.mark.timeout(1.0)
def test_equalizer_04():
    # equalizable and change doesn't affect it
    assert exam.equalizer([1, 3, 1, 3]) == [1, 2, 2, 3]
    assert exam.equalizer([3, 1, 3, 1]) == [3, 2, 2, 1]


@pytest.mark.timeout(5.0)
def test_equalizer_05():
    # random
    for _ in range(100):
        int_list = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        new_list = []
        for x, y in enumerate(int_list):
            if x == 0 or x == len(int_list) - 1:
                new_list.append(y)
            else:
                new_list.append(y + (new_list[-1] > y < int_list[x + 1]) - (new_list[-1] < y > int_list[x + 1]))
        assert exam.equalizer(int_list) == new_list
