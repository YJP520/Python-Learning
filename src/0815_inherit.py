#
# 2022/08/15 Python Learning
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

    def get_info(self):
        print(self.name, "的年龄为：", self.age)


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显式调用父类的初始化方法，不然解释器不会去调用
        self.score = score

    def get_info(self):
        print(self.name, "的年龄为：", self.age, "分数为：", self.score)


def test():
    s = Student("YJP", 21, 149)
    s.get_info()
    print(dir(s))


if __name__ == "__main__":
    test()
