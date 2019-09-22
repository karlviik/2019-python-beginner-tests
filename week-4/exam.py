

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
