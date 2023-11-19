from patten import Patten
from support import call_all_methods, cards_to_value, contain


def first_judge(input_ls: list[str]):
    try:
        # 输入不在字典中
        values_ls: list[int] = [cards_to_value[i] for i in input_ls]
    except KeyError:
        return False, 1
    return values_ls, 1


def second_judge(input_ls: list[str], cards: list[int]):
    values_ls, flag = first_judge(input_ls)
    if not values_ls:
        return False, flag
    else:
        # 输入不在手牌中
        if not contain(values_ls, cards):
            return False, 2
        else:
            return values_ls, 2


def third_judge(input_ls: list[str], cards: list[int], old: tuple):
    values_ls, flag = second_judge(input_ls, cards)
    if not values_ls:
        return False, flag
    else:
        obj = Patten(values_ls, old=old)
        result = call_all_methods(obj)
        # 牌型错误
        if result is None:
            return False, 3
        else:
            if old:
                if old[0] == result[0] and old[1] == result[1]:
                    if result[2] > old[2]:
                        return result[0], result[1], result[2], values_ls
                    else:
                        # 牌小
                        return False, 4
                elif old[0] != 'bomb' and result[0] == 'bomb':
                    return result[0], result[1], result[2], values_ls
                else:
                    return False, 3
            else:
                return result[0], result[1], result[2], values_ls
