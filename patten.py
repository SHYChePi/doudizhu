from support import count


# 牌型
class Patten:
    def __init__(self, new_ls: list[int], old: tuple = ()):

        self.card_ls: list[int] = new_ls
        self.card_nums = len(self.card_ls)
        self.card_kind_nums = len(set(self.card_ls))
        self.card_max = max(self.card_ls)
        self.card_min = min(self.card_ls)
        self.card_dic: dict[int, int] = count(self.card_ls)
        self.old: tuple = old

    def single(self):
        if self.card_nums == 1:
            return 'single', 1, self.card_ls[0]

    def double(self):
        if self.card_nums == 2 and self.card_kind_nums == 1:
            return 'double', 1, self.card_ls[0]

    def triple(self):
        if self.card_nums == 3 and self.card_kind_nums == 1:
            return 'triple', 1, self.card_ls[0]

    # 顺子

    def singles(self):
        if self.card_nums == self.card_kind_nums and self.card_nums >= 5:
            if self.card_max <= 12 and self.card_nums == self.card_max - self.card_min + 1:
                return 'singles', self.card_nums, self.card_max

    # 连对

    def doubles(self):
        if self.card_kind_nums >= 3 and self.card_max <= 12:
            if self.card_kind_nums == self.card_max - self.card_min + 1:
                for key, value in self.card_dic.items():
                    if value != 2:
                        break
                else:
                    return 'doubles', self.card_kind_nums, self.card_max

    # 三带一

    def three_with_one(self):
        if self.card_nums == 4 and self.card_kind_nums == 2:
            for key, value in self.card_dic.items():
                if value == 3 and key <= 13:
                    return 'three_with_one', 1, key

    # 三带二

    def three_with_two(self):
        if self.card_nums == 5 and self.card_kind_nums == 2:
            for key, value in self.card_dic.items():
                if value == 3 and key <= 13:
                    return 'three_with_two', 1, key

    # 炸弹

    def bomb(self):
        if self.card_nums == 2 and 14 in self.card_ls and 15 in self.card_ls:
            return 'bomb', 1, 14
        elif self.card_nums == 4 and self.card_kind_nums == 1:
            return 'bomb', 1, self.card_ls[0]

    # 四带两单牌

    def four_with_two_single(self):
        if self.card_nums == 6:
            for key, value in self.card_dic.items():
                if value == 4:
                    return 'four_with_two_single', 1, key

    # 飞机

    def airplane(self):
        print('here')
        if self.card_nums // 4 == 0 or self.card_nums // 5 == 0:
            one: list[int] = []
            two: list[int] = []
            three: list[int] = []
            for key, value in self.card_dic.items():
                if value == 3:
                    three.append(key)
                if value == 1:
                    one.append(key)
                if value == 2:
                    two.append(key)
            max_three = max(three)
            num_three = len(three)
            min_three = min(three)
            num_one = len(one)
            num_two = len(two)
            if max_three <= 12 and len(three) == max_three - min_three + 1:
                if num_three == num_one and self.card_nums == num_three * 3 + num_one:
                    return 'airplane', self.card_nums, max_three
                if num_three == num_two and self.card_nums == num_three * 3 + num_two * 2:
                    return 'airplane', self.card_nums, max_three

    # 四带两对

    def four_with_two_double(self):
        if self.card_nums == 8:
            four: list[int] = []
            two: list[int] = []
            for key, value in self.card_dic.items():
                if value == 4:
                    four.append(key)
                if value == 2:
                    two.append(key)
            if len(four) == 1 and len(two) == 2:
                return 'four_with_two_double', 1, four[0]
