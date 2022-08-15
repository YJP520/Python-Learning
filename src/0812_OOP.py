#
# 2022/08/11 Python Learning
#
# Object oriented Programming 面向对象
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

class Student:  # 类名首字母大写，多个单词驼峰原则

    def __init__(self, name, score):  # self必须位于第一个参数
        """ 构造函数 """
        self.name = name
        self.score = score

    def get_score(self):  # self必须位于第一个参数
        """ 获取分数信息 """
        print("{0}的分数为{1}".format(self.name, self.score))
        return self.score


def test():
    Stu = Student
    s1 = Student("YJP", 99)
    s2 = Stu("XX", 100)
    s1.get_score()
    s2.get_score()


class People:

    company = "Embedded"  # 类属性
    count = 0  # 类属性

    def __init__(self, name, age, score):
        self.name = name  # 实例属性
        self.age = age
        self.score = score
        People.count += 1

    def get_info(self):  # 实例方法
        print("------------------------------")
        print("- name    : {0}".format(self.name))
        print("- age     : {0}".format(self.age))
        print("- score   : {0}".format(self.score))
        print("- company : {0}".format(self.company))
        print("- count   : {0}".format(self.count))
        print("------------------------------")


def test2():
    p1 = People("YJP", 21, 99)
    p1.get_info()


class Human:
    base = "碳基生命体"  # 类属性

    @classmethod  # 类方法
    def get_base(cls):
        """ 打印信息 """
        print(cls.base)

    @staticmethod
    def add(number1, number2):  # 静态方法
        """ 加法计算 """
        sum = number1 + number2
        print("计算:S{0} + {1} = {2}".format(number1, number2, sum))
        return sum


if __name__ == '__main__':
    # test()
    # test2()
    Human.get_base()
    Human.add(45, 55)
