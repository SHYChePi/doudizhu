from random import shuffle

cards_to_value = {
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    '10': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
    '2': 13,
    'SJ': 14,
    'BJ': 15
}

value_to_card = {
    1: '3',
    2: '4',
    3: '5',
    4: '6',
    5: '7',
    6: '8',
    7: '9',
    8: '10',
    9: 'J',
    10: 'Q',
    11: 'K',
    12: 'A',
    13: '2',
    14: 'SJ',
    15: 'BJ'
}


# 判断是否为自己的回合
def check(old: tuple, turn: int, obj):
    if not turn:
        old = ()
        turn = 2
    result = obj.run(old=old)
    if not result[0]:
        turn -= 1
    return result[1], turn


def call_all_methods(obj):
    methods = [
        'single', 'double', 'triple', 'singles', 'doubles',
        'three_with_one', 'three_with_two', 'bomb', 'four_with_two_single',
        'airplane', 'four_with_two_double'
    ]
    for i in methods:
        method = getattr(obj, i)
        # print(method)
        result = method()
        if result:
            return result
        else:
            continue


# 发牌
def gen(num: int, total_cards_value: list[int] = []):
    if not total_cards_value:
        total_cards_value: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4 + [14, 15]
    player_cards_value: list[int] = []
    shuffle(total_cards_value)
    player_cards_value.extend(total_cards_value[0:num])
    del total_cards_value[0:num]
    player_cards_value = sorted(player_cards_value)
    if not total_cards_value:
        return player_cards_value
    else:
        return player_cards_value, total_cards_value


# 牌数量
def count(ls):
    counts: dict = {}
    for item in ls:
        counts[item] = counts.get(item, 0) + 1
    return counts


# ls1是否是ls2的真子集
def contain(ls1: list[str | int], ls2: list[str | int]):
    dic1 = count(ls1)
    dic2 = count(ls2)
    for i in ls1:
        if i in ls2 and dic1.get(i) <= dic2.get(i):
            pass
        else:
            return False
    else:
        return True
