#
# 2022/07/08 Python Learning
#
# 运算符
#


# 基本运算符
def test():
    a = 0b11001
    b = 0b01000
    c = a | b
    print(f"c = {c},bin(c) = {bin(c)}")
    print(f"bin(c&b) = {bin(c&b)}")
    print(f"bin(c^b) = {bin(c^b)}")
    d = 3
    print(f"d = {d},d << 2 = {d << 2}")
    d = 8
    print(f"d = {d},d >> 1 = {d >> 1}")


# Main
if __name__ == '__main__':
    test()
