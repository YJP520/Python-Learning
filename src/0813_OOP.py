#
# 2022/08/13 Python Learning
#
# Object oriented Programming 面向对象
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

# 析构函数
class Person:

    def __del__(self):
        print("销毁对象：{0}".format(self))


def test():
    p1 = Person()
    p2 = Person()
    del p2
    print("程序结束")


# 测试可调用方法__call__()
class SalaryAccount():
    """ 工资计算类 """

    def __call__(self, salary):
        print("算工资了:")
        yourSalary = salary * 12
        daySalary = salary // 22.5
        hourSalary = salary // 8

        return dict(yourSalary = yourSalary, monthSalary = salary, daySalary = hourSalary)


def test2():
    s = SalaryAccount()
    print(s(3000))


if __name__ == "__main__":
    # test()
    test2()