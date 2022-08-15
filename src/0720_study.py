#
# 2022/07/20 Python Learning
#
# 形参和实参
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)

import turtle


# 形参和实参
def printMax(a, b):
    """ 实现两个数的比较，并返回较大的值 """
    if a > b:
        print(a, '较大值')
    elif a < b:
        print(b, '较大值')
    else:
        print("a, b一样大")


def play():
    """ 快来找我玩啊 """
    print("快来找我玩啊!!!")


if __name__ == '__main__':
    printMax(10, 20)
    printMax(30, 5)
    help(play.__doc__)
    play()
