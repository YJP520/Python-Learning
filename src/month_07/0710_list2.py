#
# 2022/07/10 Python Learning
#
# 元素的添加和删除
#


# 元素的添加
def test():
    myList = [0, 2, 5, '520', True]
    print(myList)
    myList.append('I love you')
    print(myList)
    myList += ["早上好"]
    print(myList)
    print(f"len(myList) = {len(myList)}")
    myList.extend('好可爱')
    print(myList)
    myList.insert(3, "XX")
    print(myList)


# 元素的删除
def test2():
    myList = [0, 2, 5, "XX", '520', True, 'I love you', "早上好", '好可爱']
    print(myList)
    del myList[4]
    print(myList)
    print(myList.pop())
    print(myList)
    print(myList.pop(2))
    print(myList)
    myList.remove(0)
    print(myList)


# Main
if __name__ == '__main__':
    # test()
    test2()
