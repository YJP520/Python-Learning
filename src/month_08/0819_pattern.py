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

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

class CarFactory:
    def create_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

def test():
    factory = CarFactory()
    c1 = factory.create_car("奔驰")
    c2 = factory.create_car("宝马")
    c3 = factory.create_car("比亚迪")
    print(c1)
    print(c2)
    print(c3)


if __name__ == "__main__":
    test()
