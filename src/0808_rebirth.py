#
# 2022/08/08 Python Learning
#
# copy and deepcopy
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

import copy

def test_copy():
    a_list = [20, 50, [5, 6]]
    b_list = copy.copy(a_list)

    print("a : ", a_list)
    print("b : ", b_list)

    b_list.append(100)
    b_list[2].append(200)
    print("浅拷贝...")
    print("a : ", a_list)
    print("b : ", b_list)


def test_deepcopy():
    a_list = [20, 50, [5, 6]]
    b_list = copy.deepcopy(a_list)

    print("a : ", a_list)
    print("b : ", b_list)

    b_list.append(100)
    b_list[2].append(200)
    print("深拷贝...")
    print("a : ", a_list)
    print("b : ", b_list)


def test_param(a, b, *c):
    """ 可变参数 1 """
    print(a, b, c)


def test_param2(a, b, **c):
    """ 可变参数 2 """
    print(a, b, c)


if __name__ == '__main__':
    # test_copy()
    # test_deepcopy()
    test_param(8, 9, 20)
    test_param2(8, 30, name="YJP", age=18)
