"""
自定义一个模块
    实现数学的四则运算
    两个数的加减乘除运算
"""
# 手动添加全局变量__all__之后
# Python下不提倡使用
__all__ = ['add', 'sub', 'mul', 'div']  # 字符串作为元素

def add(a, b):
    """
    加法运算
    :param a:
    :param b:
    :return: 两个数的和
    """
    return a + b

def sub(a, b):
    """
    减法运算
    :param a:
    :param b:
    :return: 两个数的差
    """
    return a - b

def mul(a, b):
    """
    乘法运算
    :param a:
    :param b:
    :return: 两个数的积
    """
    return a * b

def div(a, b):
    """
    除法运算
    :param a:
    :param b:
    :return: 两个数的商
    """
    if b != 0:
        return a / b
    else:
        print("除数无意义...")
        return 0

if __name__ == '__main__':
    a = 10
    b = 2
    print("a,b的和为：%g"%add(a, b))
    print("a,b的差为：%g"%sub(a, b))
    print("a,b的积为：%g"%mul(a, b))
    print("a,b的商为：%g"%div(a, b))