#
# 2022/08/09 Python Learning
#
# lambda 表达式
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy


def test_lambda():
    """ lambda表达式 """
    f = lambda a, b, c : a + b + c
    print(f)
    print(f(2, 3, 4))

    # 每一个元素都是lambda表达式
    # 函数也是对象
    g = [lambda a:a*2, lambda b:b*3, lambda c:c*4]
    print(g[0](6), g[1](7), g[2](8))


if __name__ == '__main__':
    test_lambda()
