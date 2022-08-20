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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_name(self):
        print("我的名字为：", self.name)

    def introduce_age(self):
        print("我的年龄为：{0}".format(self.age))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显式调用父类的初始化方法，不然解释器不会去调用
        self.score = score

    def introduce_name(self):
        """ 重写父类的方法 """
        print("大家好，我的名字为：", self.name)

    def introduce_age(self):
        """ 重写父类的方法 """
        print("大家好，我的年龄为：{0}".format(self.age))


def test():
    s = Student("YJP", 21, 149)
    s.introduce_name()
    s.introduce_age()


if __name__ == "__main__":
    test()
