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

# 测试组合

class A1:
    def say_a1(self):
        print("a1:", self)

class B1:
    def __init__(self, a):
        self.a = a

def test():
    a1 = A1()
    b1 = B1(a1)
    b1.a.say_a1()


if __name__ == "__main__":
    test()