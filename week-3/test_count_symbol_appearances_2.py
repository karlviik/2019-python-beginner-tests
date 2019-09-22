import random
import string

import pytest
import exam

# input string
# output dict where key is int and value is list of symbols that appeared that many times in the string


def assert_solution(word):
    answer = exam.count_symbol_appearances_2(word)
    print(answer)
    symbol_set = set(word)
    quantity_list = []
    for symbol in symbol_set:
        quantity_list.append(word.count(symbol))
        if symbol not in answer[word.count(symbol)]:        # if symbol is not where expected
            return False
    if len(answer.keys()) != len(set(quantity_list)):       # if there are extra dictionary keys
        return False
    values = [item for sublist in list(answer.values()) for item in sublist]
    if len(values) != len(set(values)) or set(values) != symbol_set:        # if there are repeat values or extra values
        return False
    return True


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_2_01():
    # all different
    assert assert_solution("1")         # {1: ["1"]
    assert assert_solution("abc")       # {1: ["a", "b", "c"]}


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_2_02():
    # all same
    assert assert_solution("1111")      # {4: ["1"]}
    assert assert_solution("      ")    # {6: [" "]}


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_2_03():
    # various
    assert assert_solution("abba")      # {2: ["a", "b"]}
    assert assert_solution("AaAaAAAAa ")    # {1: [" "], 3: ["a"], 6: ["A"]}


@pytest.mark.timeout(1.0)
def test_count_symbol_appearances_2_04():
    # empty string
    assert assert_solution("")      # {}


@pytest.mark.timeout(5.0)
def test_count_symbol_appearances_2_05():
    # random
    for _ in range(100):
        assert assert_solution("".join(random.choices(string.ascii_letters, k=random.randint(0, 100))))
