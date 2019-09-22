def check_if_substring(a: str, b: str):
    return a in b or b in a


def reverse_string(word: str):
    return word[::-1]


def capitalise_words(sentence: str):
    return " ".join(k[0].capitalize() + k[1:] for k in sentence.split())


def multiply_string(string: str, multiply: int):
    return string * multiply


def remove_odd(numbers: list):
    return [x for x in numbers if x % 2 == 0]


def return_min(numbers: list):
    return min(numbers) if len(numbers) > 0 else None


def return_max_pos(numbers: list):
    return numbers.index(max(numbers)) if len(numbers) > 0 else -1


def starry_night(rows: int):
    return "\n".join("*" * x for x in range(1, rows + 1))


# 1 SET
# On antud list arvudest. Tagasta unikaalsete arvude väärtuste arv listis.
def count_unique(numbers: list) -> int:
    return len(set(numbers))


# 2 SET
# On antud kaks setti, tagasta, kas üks set sisaldab kõiki teise seti elemente.
def compare_sets(set1: set, set2: set) -> bool:
    return set1.difference(set2) == set() or set2.difference(set1) == set()


# 3 DICT
# On antud list sõnedest. Tagasta dict, kus võtmeks on sümbol ja väärtuseks selle sümboliga algavad sõned nende esinemise järjekorras.
def organise_by_first_symbol(strings: list) -> dict:
    dictionary = {}
    for word in strings:
        dictionary.setdefault(word[0], [])
        dictionary[word[0]] += [word]
    return dictionary


# 4 DICT
# On antud sõne. Tagasta dict, kus võtmeks on sümbol ja väärtuseks on arv, mitu korda ta sõnes esines.
def count_symbol_appearances(stringy_string: str) -> dict:
    dictionary = {}
    for symbol in stringy_string:
        dictionary.setdefault(symbol, 0)
        dictionary[symbol] += 1
    return dictionary


# 5 DICT + SET
# On antud dict. Tagasta list unikaalsetest dicti väärtustest.
def get_unique_values(dictionary: dict) -> list:
    return list(set([x for x in dictionary.values()]))


# 6 DICT + SET
# On antud sõne. Tagasta dict, kus võtmeks on täisarv ning väärtuseks on list sümbolitest, mis nii mitu korda sõnes esinesid.
def count_symbol_appearances_2(stringy_string: str) -> dict:
    dictionary = {}
    symbol_set = set(stringy_string)
    for symbol in symbol_set:
        dictionary.setdefault(stringy_string.count(symbol), [])
        dictionary[stringy_string.count(symbol)] += symbol
    return dictionary
