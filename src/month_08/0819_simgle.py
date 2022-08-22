#
# 2022/08/19 Python Learning
#
# Design Pattarm 设计模式
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy


class MySimgleton:

    __obj = None  # 类属性
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MySimgleton.__init_flag:
            print("init......")
            self.name = name
            MySimgleton.__init_flag = False

def test():
    a = MySimgleton("aa")
    b = MySimgleton("bb")
    print(a)
    print(b)
    c = MySimgleton("cc")
    print(c)


if __name__ == "__main__":
    test()