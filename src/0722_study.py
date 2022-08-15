#
# 2022/07/22 Python Learning
#
# 变量的作用域
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)

import turtle

A = 100  # 全局变量


def test():
    """变量的作用域"""
    global A  # 使用全局变量
    print(A)
    A = 300
    print(A)

    print(locals())  # 打印输出的局部变量
    print(globals())  # 打印输出的全局变量


if __name__ == '__main__':
    test()
    print(A)
