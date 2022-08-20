#
# 2022/08/17 Python Learning
#
# Object oriented Programming 面向对象 多态
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

class Man:

    def eat(self):
        print('饿饿,饭饭...')

class Chinese(Man):

    def eat(self):
        print('中国人用筷子吃饭')

class English(Man):

    def eat(self):
        print('英国人用叉子吃饭')

class Indian(Man):

    def eat(self):
        print('印度人用手吃饭饭')

def manEat(m):
    if isinstance(m, Man):
        m.eat()
    else:
        print("不能吃饭...")


def test():
    manEat(Man())
    manEat(Chinese())
    manEat(English())
    manEat(Indian())


if __name__ == "__main__":
    test()
