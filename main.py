from player import Player
from support import gen, check


def main():
    list1, rest1 = gen(20)
    p1 = Player(cards=list1, name='p1')
    list2, rest2 = gen(17, rest1)
    p2 = Player(cards=list2, name='p2')
    list3 = gen(17, rest2)
    p3 = Player(cards=list3, name='p3')
    old = ()
    turn=2
    while 1:
        old, turn=check(old,turn,p1)
        old, turn=check(old,turn,p2)
        old, turn=check(old,turn,p3)


if __name__ == '__main__':
    main()
