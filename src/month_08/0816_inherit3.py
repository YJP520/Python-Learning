#
# 2022/08/16 Python Learning
#
# Object oriented Programming 面向对象
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

class Person:  # 默认继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "名字是{0}，年龄为{1}".format(self.name, self.age)


def test():
    p = Person("YJP", 21)
    print(p)


if __name__ == "__main__":
    test()
