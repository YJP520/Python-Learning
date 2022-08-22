#
# 2022/07/17 Python Learning
#
# zip & 推导式
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)


# zip
def test():
    names = ("First", "Second", "Third", "Fourth")
    ages = (28, 26, 20, 25)
    jobs = ("老师", "程序员", "学生", "公务员")

    for name, age, job in zip(names, ages, jobs):
        print("{0}--{1}--{2}".format(name, age, job))


# 列表推导式
def test2():
    a = [x for x in range(1, 5)]
    b = [x * 2 for x in range(1, 5)]
    c = [x * 5 for x in range(1, 20) if x % 5 == 0]

    print(a)
    print(b)
    print(c)


# 字典推导式
def test3():
    # 统计文本中字符出现的次数
    myWords = "I Love You, File, Edit, All Right."
    char_count = {c: myWords.count(c) for c in myWords}
    print(myWords)
    print(char_count)


# 集合推导式
def test4():
    a = {x for x in range(1, 100) if x % 9 == 0}
    print(a)


# 生成器推导式 生成元组
def test5():
    gnt = (x for x in range(1, 100) if x % 9 == 0)
    for x in gnt:
        print(x, end=' ')
    for x in gnt:
        print(x, end=' ')


if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    # test4()
    test5()
