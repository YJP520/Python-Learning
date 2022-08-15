#
# 2022/07/05 Python Learning
#
# 字符串学习2
#

import time

# str() 数字转字符串
def test():
    a = 520
    print(f"a = {a}")
    aToString = str(a)
    print(f"aToString = {aToString}")


# []提取字符
def test2():
    myWords = "I Love You."
    print(myWords)
    print(f"myWords[0] = {myWords[0]}")
    print(f"myWords[len(myWords) - 1] = {myWords[len(myWords) - 1]}")
    print(f"myWords[-1] = {myWords[-1]}")
    print(f"myWords[-len(myWords)] = {myWords[-len(myWords)]}")


# replace()字符串替换
def test3():
    myWords = "I Love You."
    print(f"myWords = {myWords}")
    newWords = myWords.replace("You", "Moon and stars")
    print(f"newWords = {newWords}")


# slice切片 字符串提取
def test4():
    myWords = "I Love You."
    print(f"myWords[:] = {myWords[:]}")
    print(f"myWords[6:] = {myWords[2:]}")
    print(f"myWords[:6] = {myWords[:6]}")
    print(f"myWords[2:6] = {myWords[2:6]}")
    print(f"myWords[2:8:2] = {myWords[2:8:2]}")
    print(f"myWords[-3:] = {myWords[-3:]}")
    print(f"myWords[-8:-3] = {myWords[-8:-3]}")
    print(f"myWords[::-1] = {myWords[::-1]}")


# split()分隔
def test5():
    myWords = "I Love You."
    print(f"myWords.split() = {myWords.split()}")
    print(f"myWords.split('Love') = {myWords.split('Love')}")


# join()合并
def test6():
    myWords = ['I love you.', 'But,', 'love is broken.']
    print(f"''.join(myWords) = {''.join(myWords)}")


# 比较join 和 + 的效率
def cmp():
    time1 = time.time()  # 起始时刻
    a = ''
    for i in range(1000000):
        a += 'I Love You.'
    time2 = time.time()  # 终止时刻
    print(f" + 运算时间 = {time2 - time1}")

    time1 = time.time()  # 起始时刻
    li = []
    for i in range(1000000):
        li.append('I Love You.')
    a = "".join(li)
    time2 = time.time()  # 终止时刻
    print(f"join 运算时间 = {time2 - time1}")


# Main
if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    cmp()