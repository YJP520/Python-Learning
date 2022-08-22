#
# 2022/07/03 Python Learning
#
# 基础知识学习
#


# 测试程序
def test():
    # 变量赋值
    my_string = "I Love You"
    print(my_string)
    print(id(my_string))
    print(type(my_string))
    del my_string  # 删除变量


# 系列解包赋值实现变量交换
def swp():
    a, b = 520, 1314
    print(f"a = {a}, b = {b}")
    a, b = b, a  # 系列解包赋值实现变量交换
    print(f"a = {a}, b = {b}")
    del a, b


# 基本运算测试
def calculate():
    a, b = 5, 2
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a ** b}")
    print(f"divmod(a, b) = {divmod(a, b)}")
    del a, b


import time


# 显示时间
def timer():
    seconds = int(time.time())
    print(f"秒数：{seconds}")
    minutes = seconds // 60
    print(f"分钟数：{minutes}")
    hours = minutes // 60
    print(f"小时数：{hours}")
    days = hours // 24
    print(f"天数：{days}")

    del seconds, minutes, hours, days


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # test()
    # swp()
    # calculate()
    timer()
