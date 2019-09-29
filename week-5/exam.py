import string


# antud list intidest, võta kordamööda eest- ja tagantpoolt ja tagasta saadud list. nt: 1,2,3,4,5,6 => 1,6,2,5,3,4
def front_and_back(int_list: list) -> list:
    return [int_list[(z + 1) // 2 * (-1) ** z] for z in range(len(int_list))]


# järjendis sõned. jätta alles sõned, kus kaks esimest sümbolit on samad nt ["a", "bb", "bbs"] => ["bb", "bbs"]
def keep_if_first_two_symbols_same(str_list: list) -> list:
    return [x for x in str_list if len(x) > 1 and x[0] == x[1]]


# ristsumma. antakse täisarv, tuleb leida ristsumma 12 => 3, 12345 => 15
def cross_sum(integer: int) -> int:
    return sum([int(x) for x in str(abs(integer))])


# antakse list sõnedest. liida kokku sõned pikkusega 1, nt: ["a", "bb", "", "c"] => "ac"
def join_symbols(str_list: list) -> str:
    return "".join([x for x in str_list if len(x) == 1])


# arvude "tasandamine". järjend täisarvudest. arv, mis on kahe väiksema arvu vahel, tuleb vähendada.
# arv, mis asub kahe suurema arvu vahel, tuleb suurendada.
# neid täidetakse järjest (st vasakult rakendad seda reeglit järjest).
# [1, 4, 1] => [1, 3, 1]
# [1, 2] => [1, 2]
# [1, 4, 1, 0, 2] => [1, 3, 1, 1, 2]
# [1, 4, 1, 4, 1] => [1, 3, 2, 4, 1] valesiinpraegu
# [1, 2, 1, 2, 1] => [1, 1, 1, 1, 1]
def equalizer(int_list: list) -> list:
    new_list = []
    for x, y in enumerate(int_list):
        if x == 0 or x == len(int_list) - 1:
            new_list.append(y)
        else:
            new_list.append(y + (new_list[-1] > y < int_list[x + 1]) - (new_list[-1] < y > int_list[x + 1]))
    return new_list


# arvude list. tagastada list, kus on järjestikuste arvude vahe: [1, 4, 3] => [3, 1] . abs() vahe.
# [1] => []
# [1, 10, 10] => [9, 0]
def difference(int_list: list) -> list:
    return [abs(int_list[x] - int_list[x + 1]) for x in range(len(int_list) - 1)]


# antakse minutite arv (0 <= z < 1440). tagastada ennik tund, minut:
# 10 => 0, 10
# 100 => 1, 40
# 1000 => 16, 40
def minutes_to_hours_and_minutes_tuple(minutes: int) -> tuple:
    return minutes // 60, minutes - 60 * (minutes // 60)


# sõne. tagastada sõne, kus on algse sõne iga teine sümbol: "tere" => "tr"
# "abcdef" => "ace"
def every_second_symbol(stringy: str) -> str:
    return stringy[::2]


# sõne väikestest ladina tähtedest. kahe kõrvutioleva tähe vahe. "abc" => [1, 1]
# "ada" => [3, -1]
# "a" => []
# "akm" => [10, 2]
def get_symbol_differences(stringy: str) -> list:
    return [string.ascii_lowercase.find(stringy[x]) - string.ascii_lowercase.find(stringy[x - 1]) for x in range(1, len(stringy))]


# eelmise pöördfunktsioon. antakse esimene täht ja list tähede vahest:
# "a", [1, 1] => "abc"
# "a", [] => "a"
# "a", [10, -2] => "aki"
def build_from_symbol_difference(stringy: str, differences: list) -> str:
    return "".join([string.ascii_lowercase[string.ascii_lowercase.find(stringy) + sum(differences[:x])] for x in range(len(differences) + 1)])
