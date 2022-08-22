#
# 2022/07/16 Python Learning
#
# 控制语句2
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)


# 嵌套循环
def test():
    for i in range(5):
        for j in range(6):
            print(f"{i}", end='')
        print('')  # 换行


# 九九乘法表
def test2():
    for i in range(1, 10):
        for j in range(1, i):
            # print(f"{i}*{j}={i * j}", end='  ')
            print("{0}*{1}={2}".format(i, j, i*j), end='  ')
        print("")


# 表格
def test3():
    staff1 = dict(name='高小一', age=20, salary=30000, city='北京')
    staff2 = dict(name='高小二', age=19, salary=20000, city='上海')
    staff3 = dict(name='高小幺', age=18, salary=10000, city='深圳')
    table = [staff1, staff2, staff3]

    for x in table:
        if x.get("salary") > 15000:
            print(x)


# Main
if __name__ == '__main__':
    # test()
    # test2()
    test3()
