#
# 2022/08/23 Python Learning
#
# 异常处理
#

# 抛出异常 raise 异常对象

# 定义一个异常类
class GenderException(Exception):
    def __init__(self):
        super().__init__()
        self.errMsg = '性别只能设置成男或者女'

class Student():
    def __init__(self, name, gender):
        self.name = name
        self.setGender(gender)

    #设置性别
    def setGender(self, gender):
        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            # 抛出异常 性别异常
            raise GenderException()

    def getGender(self):
        return self.__gender
    def showInfo(self):
        print("我叫:%s, 性别:%s"%(self.name, self.__gender))


if __name__ == '__main__':
    stu = Student('学生1', '男')
    try:
        stu.setGender('不男不女')
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e.errMsg)
    stu.showInfo()




def test1():
    a = input("请输入被除数：")
    b = input("请输入除数：")

    try:
        a = int(a)
        b = int(b)
        c = a / b
        print('商为:%g'%c)
    except ValueError:
        print('数据类型有误')
    except ZeroDivisionError:
        print('除数不能为0')
    except Exception:
        print('其他异常')

def test2():
    try:
        # 打开文件
        file = open('TestFile.txt', 'w', encoding='utf-8')
        print('文件打开成功')
        # 文件写入 write只能将字符串数据写入到文件
        file.write('Hello World...')
        # file.write([1, 2, 3])  # 报错
    except Exception as e:
        print(e.args)
    else:
        print('文件写入完毕')
    finally:
        # 文件关闭
        file.close()
        print('关闭文件，谢谢试用')