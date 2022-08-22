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

class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0}--{1}".format(self.name, other.name)
        else:
            return "不是同类对象，故不能相加。"

def test():
    P1 = Person("YJP")
    P2 = Person("XX")
    x = P1 + P2
    print(x)


if __name__ == "__main__":
    test()