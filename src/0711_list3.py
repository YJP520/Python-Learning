#
# 2022/07/11 Python Learning
#
# 列表基本操作
#

import random


# 切片操作
def test():
    num = [10, 20, 30, 40, 50, 60]

    print(num[1:3:1])
    print(num[1::2])
    print(num[1:4])
    print(num[-5:-1])
    print(num[::-1])  # 逆序


# 遍历操作
def test2():
    num = [10, 20, 30, 40, 50, 60]
    for i in num:
        print(f"{i},", end='')


# 排序函数
def test3():
    num = [10, 20, 30, 40, 50, 60]
    for i in num:  # 遍历列表
        print(f"{i},", end='')
    print('')
    random.shuffle(num)  # 打乱数组
    for i in num:  # 遍历列表
        print(f"{i},", end='')
    print('')
    num.sort(reverse=True)
    for i in num:  # 遍历列表
        print(f"{i},", end='')
    print('')


# 二维列表
def test4():
    table = [
        ["PEI", 21, '北京'],
        ["XIA", 20, '北京'],
        ["XXX", 24, '北京'],
    ]
    print(table)
    # 列表的遍历
    for i in range(3):
        for j in range(3):
            print(table[i][j], end='\t')
        print()  # 打印完一行后换行


# Main
if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    test4()
