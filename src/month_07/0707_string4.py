#
# 2022/07/07 Python Learning
#
# 字符串学习4
#

import io

# format()基本用法
def test():
    info1 = "名字：{0}，年龄：{1}。"
    print(info1.format("YJP", 20))

    info2 = "名字：{0}，年龄：{1}。{0}学习Python。"
    print(info2.format("YJP", 20))

    info3 = "名字：{name}，年龄：{age}。"
    print(info3.format(name='YJP', age=20))


# 填充和对齐
def test2():
    print("{:*>8}".format("520"))
    print("我是{0},我喜欢数字{1:*<8}".format("YJP", "520"))


# 数字格式化
def test3():
    str1 = "3.1415926格式化为{0:.2f}"
    print(str1.format(3.1415926))


# 可变字符串 import io
def test4():
    myWords = "520,**"
    myWordsIo = io.StringIO(myWords)
    print(myWordsIo)
    print(myWordsIo.getvalue())
    print(myWordsIo.seek(4))
    print(myWordsIo.write("XX"))
    print(myWordsIo.getvalue())


# Main
if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    test4()
