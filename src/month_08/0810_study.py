#
# 2022/08/10 Python Learning
#
# 基本函数
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

def test_eval():
    """ eval函数 """
    str = "print('string')"
    eval(str)

    a = 10
    b = 20
    c = eval("a+b")
    print("c = {0}".format(c))


def test_01(n):
    """ 递归函数 """
    print("*test01,n = ", n)
    if(n == 0):
        print("over...")
    else:
        test_01(n - 1);
    print("*test01,n = ", n)


def factorial(number):
    """ 递归算阶乘 """
    if number == 1:
        return 1;
    else:
        return number * factorial(number - 1);


def test_02():
    """ 嵌套函数 """
    print('outer running')

    def inner01():
        """ 只能内部可用 """
        print('inner01 running')

    inner01()


def outer():
    b = 10

    def inner():
        nonlocal b  # 声明外部函数的局部变量
        print("inner b:",b)
        b = 20

    inner()
    print("outer b:", b)


# 测试 LEGB
str = "global"
def outer():
    str = "outer"

    def inner():
        str = "inner"
        print(str)

    inner()

outer()

if __name__ == '__main__':
    # test_01(5)
    # print("5! = {0}".format(factorial(5)))
    # test_02()
    outer()