import os
from support import value_to_card
from judge import third_judge


class Player:
    def __init__(self, cards: list[int], name):
        self.cards = cards
        self.name = name

    # 显示玩家手中的牌
    def show(self):
        ls: list[str] = []
        for i in self.cards:
            ls.append(value_to_card[i])
        print(f'{self.name}剩余手牌{ls}\n')

    # 出牌
    def input_ls(self):
        print(f'{self.name}请出牌\n')
        ls_str: list[str] = input().strip(',').strip(' ').replace(' ', ',').split(',')
        if ls_str[0] == '':
            return False
        else:
            return ls_str

    # 斗地主，启动！
    def run(self, old):
        print()
        self.show()
        while 1:
            ls_str = self.input_ls()
            if not ls_str:
                print(f'{self.name}要不起')
                return False, old

            result = third_judge(ls_str, self.cards, old)
            if not result[0]:
                if result[1] == 1:
                    print(f'{self.name}输入不在字典中')
                elif result[1] == 2:
                    print(f'{self.name}输入不在手牌中')
                elif result[1] == 3:
                    print(f'{self.name}输入为错误牌型')
                elif result[1] == 4:
                    print(f'{self.name}你的牌打的也太小了！')
                continue
            else:
                for i in result[-1]:
                    self.cards.remove(i)
                if not self.cards:
                    print(f'{self.name}赢赢赢')
                    os.system('chcp 65001')
                    os.system('pause')
                    quit()
                self.show()
                return True, result[:-1]
