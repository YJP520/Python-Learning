#
# 2022/07/15 Python Learning
#
# 控制语句
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)


# 单分支选择结构
def test():
    while True:
        num = input("请输入一个数:")
        if int(num) == 0:
            print('num == 0')
            break  # 退出循环

        if int(num) < 0:
            print('num < 0')
        if int(num) > 0:
            print('num > 0')
    del num


# 双分支选择结构
def test2():
    while True:
        num = input("请输入一个数:")
        if int(num) == 0:
            print('num == 0')
            break  # 退出循环

        if int(num) < 0:
            print('num < 0')
        else:
            print('num > 0')
    del num


# 三元条件运算符
def test3():
    while True:
        num = input("请输入一个数:")
        print(num if int(num) < 10 else "num > 10")

        if int(num) == 0:
            print('退出循环')
            break  # 退出循环
    del num


# 多分支选择结构
def test4():
    while True:
        score = input("请输入分数:")
        if int(score) < 0 or int(score) > 100:
            print("退出查询")
            break  # 退出循环

        elif int(score) < 60:
            print('成绩不及格')
        elif int(score) < 70:
            print('成绩及格')
        elif int(score) < 80:
            print('成绩中等')
        elif int(score) < 90:
            print('成绩良好')
        elif int(score) <= 100:
            print('成绩优秀')

    del score


# for 循环
def test5():
    sum = 0
    for i in range(10):
        sum += i
    print(sum)

    for x in (10, 20, 30):
        print(x * 10)

    d = {'name': 'YJP', 'age': 21}
    for x in d:
        print(x)
    for x in d.keys():
        print(x)
    for x in d.values():
        print(x)


# 100以内的奇偶数和
def test6():
    sum_all = 0
    sum_odd = 0
    sum_even = 0
    for x in range(101):
        sum_all += x
        if x % 2 == 1:
            sum_odd += x
        else:
            sum_even += x

    print("0-100累加总和{0},奇数和{1}，偶数和{2}".format(sum_all, sum_odd, sum_even))


# Main
if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    # test4()
    # test5()
    test6()
