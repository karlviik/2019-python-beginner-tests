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



# 1) antud list intidest, tagasta summa neist elementidest, mis on summa enda kahele eelmisele elemendile.
# Kui pole, siis 0
def sum_of_sum_of_two_previous_elements_elements(int_list: list) -> int:
    int_sum = 0
    for i in range(2, len(int_list)):
        if int_list[i - 2] + int_list[i - 1] == int_list[i]:
            int_sum += int_list[i]
    return int_sum


# 2) antud list sõnedest, tagasta kõige pikem sõne listist, selle puudumisel None
def longest_string(str_list: list) -> str:
    longest_str = None
    longest_length = -1
    for string in str_list:
        if len(string) > longest_length:
            longest_length = len(string)
            longest_str = string
    return longest_str


# 3) on antud sõne, tagasta selliste sümbolite arv, mis sõne tagantpoolt lugedes kattuvad sõne eestpidi lugemisega. Vms.
def reverse_string_overlap_symbols(stringy: str) -> int:
    count = 0
    for i in range(0, len(stringy)):
        if stringy[i] == stringy[-1 - i]:
            count += 1
    return count


# 4) on antud sõne, tagasta int list sõnes esinevatest numbrites nende esinemise järjekorras
def numbers_in_string(stringy: str) -> list:
    int_list = []
    for symbol in stringy:
        if symbol.isnumeric():
            int_list.append(int(symbol))
    return int_list


# 5) on antud sõne komade ja numbritega, tagasta list neist komaga eraldatud arvudest
def numbers_and_commas(stringy: str) -> list:
    return [int(i) for i in stringy.strip(",").split(",")] if len(stringy.strip(",")) != 0 else []


# 6) on antud sõne, tagasta number, mis on moodustatud sõnes esinevatest numbritest nende esinemise järjekorras.
# Kui pole, siis 0
def number_from_string(stringy: str) -> int:
    return int("".join([i for i in "0" + stringy if i.isnumeric()]))


# 7) on antud sõne numbrite, miinuste ja plussidega. Parse'i see tehe ja tagasta vastus. Kahte tehtemärki pole järjest
def addition_and_subtraction(stringy: str) -> int:
    result = 0
    current_number = "0"
    for symbol in stringy:
        if not symbol.isnumeric():
            result += int(current_number)
            current_number = ""
        current_number += symbol
    return result + int(current_number)
