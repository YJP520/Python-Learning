#
# 2022/07/12 Python Learning
#
# 字典
#

import random


# 通过{} 创建字典
def test():
    myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
    print(myDictionary)
    print(myDictionary.get('name'))
    print(myDictionary.get('gae'))
    print(myDictionary.get('job'))


# 通过dict 创建字典
def test2():
    myDictionary = dict(name='YJP', age=21, job='Engineer')
    print(myDictionary)
    print(myDictionary.get('name'))
    print(myDictionary.get('gae'))
    print(myDictionary.get('job'))


# Main
if __name__ == '__main__':
    # test()
    test2()
