#
# 2022/07/04 Python Learning
#
# 字符串学习
#


# hello string
def test(myWords):
    print(myWords)


def test2():
    print(f"ord('A') = {ord('A')}")
    print(f"chr(72) = {chr(72)}")
    print(f"ord('霞') = {ord('霞')}")


def test3():
    myWords1 = 'You are my only one.'
    print(myWords1)
    print(f"len(myWords1) = {len(myWords1)}")
    myWords2 = "Love you love your cat."
    print(myWords2)
    print(f"len(myWords2) = {len(myWords2)}")
    myWords3 = '''
    name = "YJP" 
    address = "B222"
    age = 21
    lover = "X" '''
    print(myWords3)
    print(f"len(myWords3) = {len(myWords3)}")
    myWords4 = ""
    print(f"len(myWords4) = {len(myWords4)}")


# 转义字符
def test4():
    myWords1 = '\twhat\'s up!\n'
    myWords2 = "\t\"今宵绝胜无人共，\n\
\t 卧看星河尽意明。\"\n"
    print(myWords1)
    print(myWords2)


# 字符串拼接
def test5():
    myWords1 = 'Noting is important.'
    myWords2 = 'If you leave.'
    print(myWords1 + myWords2)
    print('If you leave.' 'Noting is important.')


# 不换行打印
def test6():
    myWords1 = 'Noting is important but you.'
    print(myWords1, end="\n")
    myWords2 = 'I stand there.'
    print(myWords2, end="")


# 输入数据
def test7():
    youWords = input("请输入你的回答：")
    print("Ok. Get it.")


# Main
if __name__ == '__main__':
    # test("I love you but
    # you don't have any feelings.")
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    test7()
