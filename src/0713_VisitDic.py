#
# 2022/07/13 Python Learning
#
# 字典元素的访问
#

import random


# 通过[键]获得“值”
def test():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    print(myDictionary['name'])
    print(myDictionary['age'])
    print(myDictionary['job'])


# 通过get()获得“值”
def test2():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    print(myDictionary.get('name'))
    print(myDictionary.get('gae'))
    print(myDictionary.get('job'))


# 列出所有的键值对
def test3():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    print(myDictionary.items())


# 列出所有的键 列出所有的值
def test4():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    print(myDictionary.keys())
    print(myDictionary.values())


# 添加 键值对
def test5():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    myDictionary['love'] = 'STM32'
    myDictionary['job'] = 'Embedded'

    print(myDictionary)


# 使用update()
def test6():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    herDictionary = {'name': 'XX', 'age': 20, 'job': 'Engineer'}
    print(myDictionary)

    myDictionary.update(herDictionary)

    print(myDictionary)


# 使用popitem()
def test7():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    myDictionary.popitem()
    print(myDictionary)
    myDictionary.popitem()
    print(myDictionary)


# 序列解包
def test8():
    x, y, z = 10, 20, 30
    print(x)

    (a, b, c) = (40, 50, 60)
    print(b)

    [e, f, g] = [70, 80, 90]
    print(g)


# 序列解包 字典
def test9():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)

    # 默认对 键 进行操作
    name, age, job = myDictionary
    print(name)

    # 对 键值 对进行操作
    name2, age2, job2 = myDictionary.items()
    print(name2)

    # 对 值 对进行操作
    name3, age3, job3 = myDictionary.values()
    print(name3)


# Main
if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    test9()


