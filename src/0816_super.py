#
# 2022/08/16 Python Learning
#
# Object oriented Programming 面向对象
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

class A:

    def say(self):
        print("A:", self)


class B(A):

    def say(self):
        # A.say(self)
        super().say()
        print("B:", self)


def test():
    B().say()


if __name__ == "__main__":
    test()
