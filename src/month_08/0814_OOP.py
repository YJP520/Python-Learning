#
# 2022/08/14 Python Learning
#
# Object oriented Programming 面向对象
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

# 测试私有属性
class Employee:

    __company = "百战程序员"  # 类变量

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age  # 私有属性
        self.__salary = salary

    def __work(self):  # 私有方法
        print("{0}要好好工作".format(self.name))
        print("年龄:{0}".format(self.age))
        print("公司:{0}".format(self.__company))

    # 测试@property的最简化使用
    @property
    def salary(self):
        print("salary run...")
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误！薪水在1000--50000的范围内。")



def test():
    e = Employee("YJP", 21, 3000)
    print(e.name)
    print(e.age)
    print(e._Employee__salary)
    # print(dir(e))

    e._Employee__work()
    print(Employee._Employee__company)

    print(e.salary)
    e.salary = -2000
    print(e.salary)
    e.salary = 40000
    print(e.salary)


if __name__ == "__main__":
    test()