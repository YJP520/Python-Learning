#
# 2022/07/06 Python Learning
#
# 字符串学习3
#

import time


# 常用查找方法
def test():
    myWords = "\n\t明月如霜，好风如水，清景无限。\n\
    曲港跳鱼，圆荷泻露，寂寞无人见。\n\
    紞如三鼓，铿然一叶，黯黯梦云惊断。\n\
    夜茫茫，重寻无处，觉来小园行遍。\n\n\
    天涯倦客，山中归路，望断故园心眼。\n\
    燕子楼空，佳人何在，空锁楼中燕。\n\
    古今如梦，何曾梦觉，但有旧欢新怨。\n\
    异时对，黄楼夜景，为余浩叹。\n"

    print(myWords)
    print(f"len(myWords) = {len(myWords)}")

    print(f"myWords.startswith('\\n\\t明月如霜，好风如水，清景无限。') = ", end="")
    print(myWords.startswith('\n\t明月如霜，好风如水，清景无限。'))

    print(f"myWords.endswith('异时对，黄楼夜景，为余浩叹。\\n') = ", end="")
    print(myWords.endswith('异时对，黄楼夜景，为余浩叹。\n'))

    print(f"myWords.find('佳人') = {myWords.find('佳人')}")
    print(f"myWords.rfind('佳人') = {myWords.rfind('佳人')}")

    print(f"myWords.count('人') = {myWords.count('人')}")
    print(f"myWords.isalnum() = {myWords.isalnum()}")


# 去除首尾信息
def test2():
    myWords = "---只愿君心似我心，定不负相思意。---"
    print(f"\nmyWords = {myWords}")
    print(f"myWords.strip('-') = {myWords.strip('-')}")
    print(f"myWords.lstrip('-') = {myWords.lstrip('-')}")
    print(f"myWords.rstrip('-') = {myWords.rstrip('-')}")


# 大小写转换
def test3():
    myWords = "you are my only one."
    print(f"\nmyWords = {myWords}")
    print(f"myWords.capitalize() = {myWords.capitalize()}")
    print(f"myWords.title() = {myWords.title()}")
    print(f"myWords.upper() = {myWords.upper()}")
    print(f"myWords.lower() = {myWords.lower()}")
    print(f"myWords.swapcase() = {myWords.swapcase()}")


# 格式排版
def test4():
    myWords = "Thank you."
    print(f"\nmyWords = {myWords}")
    print(f"myWords.center(20) = {myWords.center(20)}")
    print(f"myWords.center(20, '*') = {myWords.center(20, '*')}")
    print(f"myWords.ljust(20, '*') = {myWords.ljust(20, '*')}")
    print(f"myWords.rjust(20, '*') = {myWords.rjust(20, '*')}")


# Main
if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    test4()
