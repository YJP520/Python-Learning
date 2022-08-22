#
# 2022/07/14 Python Learning
#
# 表格
#

import random
import this  # print(this.v)


# 创建表格
def createTable():
    staff1 = {'name': 'YJP', 'age': 21, 'city': '北京', 'job': 'Engineer'}
    staff2 = {'name': 'XX', 'age': 20, 'city': '上海', 'job': 'Engineer'}
    staff3 = {'name': 'ZHJ', 'age': 26, 'city': '上海', 'job': 'AI'}
    table = [staff1, staff2, staff3]

    # 获得第二行的人的name
    print("获得第二行的人的name:")
    print(table[1].get('name'))

    # 打印表中所有的年龄
    print("打印表中所有的年龄:")
    for i in range(len(table)):  # i --> 0, 1, 2
        print(table[i].get('age'))

    # 打印表的所有数据
    print("打印表的所有数据:")
    for i in range(len(table)):
        print(table[i].get('name'), table[i].get('age'), table[i].get('city'), table[i].get('job'))


# 使用 {} 创建集合
def test():
    mySet = {10, 20, 30}
    print(mySet)
    mySet.add(520)
    print(mySet)


# 使用 set() 创建集合
def test2():
    a = ['a', 'b', 'c', 'd']
    mySet = set(a)
    print(mySet)


# 集合的运算
def test3():
    mySet = {'embedded', 'vue', 'nature', 'space'}
    print(mySet)
    herSet = {'web', 'vue', 'others'}
    print(herSet)

    # 并集
    print(mySet | herSet)
    print(mySet.union(herSet))

    # 交集
    print(mySet & herSet)
    print(mySet.intersection(herSet))

    # 差集
    print(mySet - herSet)
    print(mySet.difference(herSet))


# Main
if __name__ == '__main__':
    # createTable()
    # test()
    # test2()
    test3()

