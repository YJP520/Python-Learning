#
# 2022/07/21 Python Learning
#
# 函数的返回值
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)

import turtle


def add(a, b):
    """ 计算两个数[a 和 b]的和 """
    print("计算两个数的和：{0}，{1}，{2}".format(a, b, a+b))
    return a+b


def test(x, y, z):
    """ 返回各自乘以10之后的值 """
    return [x*10, y*10, z*10]


if __name__ == '__main__':
    # c = add(30, 40)
    # print("c = ", c)
    print(test(1, 2, 3))
