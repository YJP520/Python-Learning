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


class Study:
    pass


def test():
    student1 = Student("YJP", 99)  # 调用构造函数
    student1.get_score()
    print(student1.__dict__)
    print(dir(student1))
    print(isinstance(student1, Student))


if __name__ == '__main__':
    test()