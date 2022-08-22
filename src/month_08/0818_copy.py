#
# 2022/08/18 Python Learning
#
# Object oriented Programming 面向对象
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

import copy

class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("算你个！@#￥%……&*")
        print("CPU对象:", self)

class Screen:
    def show(self):
        print("显示一个好看的画面，亮瞎你的钛合金大眼")
        print("Screen对象:", self)

def test():
    c1 = CPU()
    c2 = c1
    print(c1)
    print(c2)

    s1 = Screen()
    m1 = MobilePhone(c1, s1)
    m2 = copy.copy(m1)
    print(m1)
    print(m1.cpu)
    print(m1.screen)

    print(m2)
    print(m2.cpu)
    print(m2.screen)

    m3 = copy.deepcopy(m1)
    print(m3)
    print(m3.cpu)
    print(m3.screen)


if __name__ == "__main__":
    test()