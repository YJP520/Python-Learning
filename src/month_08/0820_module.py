#
# 2022/08/20 Python Learning
#
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)
# import copy

# 1.导入模块的方式
# import random
# result = random.randint(1, 100)
# print(result)


# import MyMath
# if __name__ == '__main__':
#     a = 10
#     b = 2
#     print("a,b的和为：%g"%MyMath.add(a, b))
#     print("a,b的差为：%g"%MyMath.sub(a, b))
#     print("a,b的积为：%g"%MyMath.mul(a, b))
#     print("a,b的商为：%g"%MyMath.div(a, b))


# 2.导入模块中相关数据的方式
# from random import randint
# result = randint(1, 100)  # 直接使用
# print(result)

# from MyMath import add, sub, mul, div
# if __name__ == '__main__':
#     a = 10
#     b = 2
#     print("a,b的和为：%g"%add(a, b))
#     print("a,b的差为：%g"%sub(a, b))
#     print("a,b的积为：%g"%mul(a, b))
#     print("a,b的商为：%g"%div(a, b))

# from MyMath import *  # 导入全部
# if __name__ == '__main__':
#     a = 10
#     b = 2
#     print("a,b的和为：%g"%add(a, b))
#     print("a,b的差为：%g"%sub(a, b))
#     print("a,b的积为：%g"%mul(a, b))
#     print("a,b的商为：%g"%div(a, b))

from src.package1.MyMath import *  # 导入全部
if __name__ == '__main__':
    a = 10
    b = 2
    print("a,b的和为：%g"%add(a, b))
    print("a,b的差为：%g"%sub(a, b))
    print("a,b的积为：%g"%mul(a, b))
    print("a,b的商为：%g"%div(a, b))
