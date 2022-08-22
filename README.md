# Python-Learning
2022/07/01 - Pycharm - Python Learning.

# **Python Learning 2022**
---

## ***2022.07.01 DAY1***

### **1. 第一个python源程序**

    # First python program.
    def print_hi(name):
        # 在下面的代码行中使用断点来调试脚本。
        print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
        print("今宵绝胜无人共，卧看星河尽意明。")
        print("别后不知君远近。触目凄凉多少闷。")
        print("小轩独坐相思处，情绪好无聊。")

    # 按间距中的绿色按钮以运行脚本。
    if __name__ == '__main__':
        print_hi('PyCharm')

### **2. 注意：**
- 不要在程序中，行开头处添加空格，空格在python中有缩进的含义。
- 符号都是英文符号，如:;''""。

### **3. 程序的基本格式**

1. 恰当的空格，缩进问题；
    - 逻辑首行的空白用来决定逻辑的缩进层次，从而决定语句的分组
    - 语句从新行的第一列开始
    - 缩进风格统一
        - 单个制表符或4个空格
        - Python用缩进而不是{}，来表示程序块
2. Python区分大小写；
3. 注释
    - 行注释
        - 每行注释前加#。
    - 段注释
        - 使用三个连续''' 人生苦短 ''',类似/* 人生苦短 */


### **4. 示例**

    # 海龟绘图代码
    import turtle
    t = turtle.Pen()

    for x in range(360):
        t.forward(x)
        t.left(49)
---
## ***2022.07.02 DAY2***
### **1. 学习图形化程序设计**
#### 1. 基础函数
    import turtle               # 导入turtle模块

    # 图形化界面学习 turtle
    def turtle_study():
        turtle.showturtle()     # 显示箭头
        turtle.write("YJP")     # 写字符串
        turtle.forward(300)     # 前继300像素
        turtle.color("red")     # 画笔颜色改成红色
        turtle.left(90)         # 箭头左转90度
        turtle.forward(300)
        turtle.goto(0, 50)      # 去坐标(0,50) 会划线
        turtle.goto(0, 0)       # 去坐标(0,0)
        turtle.penup()          # 抬笔 不划线
        turtle.goto(0, 300)     # 去坐标(0,300)
        turtle.goto(0, 0)       # 去坐标(0,0)
        turtle.pendown()        # 放笔 画线
        turtle.goto(0, 50)      # 去坐标(0,50)
        turtle.goto(50, 0)      # 去坐标(50,0)
        turtle.circle(100)      # 画圆 半径100


    # 按间距中的绿色按钮以运行脚本。
        if __name__ == '__main__':
            turtle_study()

#### 2. 奥运五环
    import turtle               # 导入turtle模块

    # 奥运五环
    def OlympicFiveCircles():
        turtle.width(10)        # 画笔宽度

        turtle.color("blue")    # 画笔颜色
        turtle.circle(50)       # 画圆1

        turtle.penup()          # 抬笔 不划线
        turtle.goto(120, 0)     # 移动
        turtle.pendown()        # 放笔 画线
        turtle.color("black")   # 画笔颜色改成红色
        turtle.circle(50)       # 画圆2

        turtle.penup()          # 抬笔 不划线
        turtle.goto(240, 0)     # 移动
        turtle.pendown()        # 放笔 画线
        turtle.color("red")     # 画笔颜色改成红色
        turtle.circle(50)       # 画圆3

        turtle.penup()          # 抬笔 不划线
        turtle.goto(60, -50)    # 移动
        turtle.pendown()        # 放笔 画线
        turtle.color("yellow")  # 画笔颜色改成红色
        turtle.circle(50)       # 画圆4

        turtle.penup()          # 抬笔 不划线
        turtle.goto(180, -50)   # 移动
        turtle.pendown()        # 放笔 画线
        turtle.color("green")   # 画笔颜色改成红色
        turtle.circle(50)       # 画圆5


    # 按间距中的绿色按钮以运行脚本。
    if __name__ == '__main__':
        OlympicFiveCircles()

### **2. python程序的构成**
#### 1. 程序构成
- Python程序由模块组成。一个模块对应一个python源文件，一般后缀名是：.py。
- 模块由语句组成。运行Python程序时，按照模块中语句的顺序依次执行。
- 语句是Python程序的构造单元，用于创建对象、变量赋值、调用函数、控制语句等。

#### 2. 编写事项
- ctr + s 保存文件
- 写好注释 #  ''' '''
- 行连接符 \ -> 用于语句太长的换行编写

### **3. 对象**
#### 1. Python中，一切皆对象
- 每个对象由：标识(identity)、类型(type)、值(value)组成。
- 对象的本质：一个内存块，拥有特定的值，支持特定类型的相关操作。

        # 变量赋值
        a = 3
        b = "I Love You"


        # 测试程序
        def test():
            print(a)
            print(id(3))
            print(id(a))
            print(type(3))
            print(type(a))

            print(b)
            print(id(b))
            print(type(b))


        # 按间距中的绿色按钮以运行脚本。
        if __name__ == '__main__':
            test()

#### 2. 引用
在python中，变量也称为：对象的引用。因为，变量存储的就是对象的地址。变量通过地址引用了对象。
- **Python是动态类型语言**
    - 变量不许要显式声明类型。根据变量引用的对象，Python解释器自动确定数据类型。
- **Python是强类型语言**
    - 每个对象都有数据类型，只支持该类型支持的操作。


---
## ***2022.07.03 DAY3***
### **1. 标识符**
- 用于变量、函数、类、模块等的名称。
    - 区分大小写。
    - 第一个字符为字母、下划线。其后字符：字母、数字、下划线。
    - 不能使用关键字。
    - 以双下划线开头和结尾的名称通常有特殊含义。如：__ init __

### **2. 标识符命名规则**
约定俗成：
- 模块和包名
    - 全小写字母。多个单词之间用下划线隔开。
- 函数名
    - 全小写字母，多个单词之间用下划线隔开。
- 类名
    - 首字母大写，采用驼峰原则。
- 常量名
    - 全大写字母，多个单词使用下划线隔开。

### **3. 变量的声明**
- 变量在使用前必须先被初始化（赋值）
- 删除变量和垃圾回收机制
- del语句删除不再使用的变量

        # 测试程序
        def test():
            # 变量赋值
            my_string = "I Love You"
            print(my_string)
            print(id(my_string))
            print(type(my_string))
            del my_string


        # 按间距中的绿色按钮以运行脚本。
        if __name__ == '__main__':
            test()
- 删除变量之后，如果对象没有变量引用，这时就会被垃圾回收器回收，清空内存空间。

### **4. 变量的赋值**
- 链式赋值
    - 同一个对象赋给多个变量：x = y = 123
- 系列解包赋值
    - 系列数据赋值给对应相同个数的变量（个数保持一致）。如：a,b,c, = 4,5,6 相当于 a=4 b=5 c=6
    - 使用系列解包赋值实现变量交换。如：a,b=1,2  a,b=b,a

            # 系列解包赋值实现变量交换
            def swp():
                a, b = 520, 1314
                print(f"a = {a}, b = {b}")
                a, b = b, a  # 系列解包赋
                print(f"a = {a}, b = {b}")


            # 按间距中的绿色按钮以运行脚本。
            if __name__ == '__main__':
                swp()
- 常量
    - 逻辑上是可以不可改的，实际上是可以改的。

### **5. 基本内置数据类型**
- 整型
    - 整数
- 浮点型
    - 小数
- 布尔型
    - 表示真假
- 字符串型
    - 字符串
- 基本运算
    - "+"   加法运算
    - "-"   减法运算
    - "*"   乘法运算
    - "/"   浮点数除法运算
    - "//"  整数除法运算
    - "%"   模（取余）运算
    - "**"  幂运算：2\**3=8
- 除数不能为零
- 使用divmod()函数同时得到商和余数：divmod(13,3)

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


        # 按间距中的绿色按钮以运行脚本。
        if __name__ == '__main__':
            calculate()

### **6. 整数**
- python中，除10进制，还有其他三种进制：
    - 0b或0B，二进制 0,1
    - 0o或0O，八进制 0,1,2,3,4,5,6,7
    - 0x或0X，十六进制 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f
- 使用int()实现类型转换
    - 浮点数直接舍去小数部分。如：int(9.9)结果为：9
    - 布尔值True转为1，False转为0。
    - 字符串符合整型格式则直接转成对应整数，否则报错。
- 自动转型
    - 整数与浮点数运算，结果自动转成浮点数
- Python2中，int是32位，long为64位。
- Python3中，int可以存储任意大小的整数。long被取消。
- Googol = 10**100
- Python3中可以做超大数运算，而不会造成“整数溢出”，这也是Python特别适合科学运算的原因。

### **7. 浮点数**
- 浮点数，float
    - 浮点数使用科学计数法表示。
- 类型转换和四舍五入
    - 使用float()将其他类型转化成浮点数。
    - 整数与浮点数运算，结果自动转成浮点数。
    - round(value)可以返回四舍五入的值。不改变原来的值。
- 增强型赋值运算符
    - "+=" a += 2 <=> a = a + 2
    - "-=" a -= 2 <=> a = a - 2
    - "*=" a *= 2 <=> a = a * 2
    - "/=" a /= 2 <=> a = a / 2
    - "//=" a //= 2 <=> a = a // 2
    - "**=" a **= 2 <=> a = a ** 2
    - "%=" a %= 2 <=> a = a % 2
- 中间不加空格。

### **8. 时间的表示**
- 计算机时间的表示是从"1970年1月1日00:00:00"开始，以毫秒（1/1000秒）进行计算。
- 使用time.time()获得当前时刻，返回的值是以秒为单位，带微秒（1/1000毫秒）的浮点值。import time

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
            timer()

### **8. 小测试**
- 定义多点坐标，绘出折线，计算起始点和终点的距离

        import turtle  # 导入海龟绘图包
        import math  # 导入数学包


        def locate():
            # 定义多个点的坐标
            x1, y1 = 100, 100
            x2, y2 = 200, -100
            x3, y3 = -100, -100
            x4, y4 = -100, 300

            # 绘制折线
            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.goto(x2, y2)
            turtle.goto(x3, y3)
            turtle.goto(x4, y4)

            # 计算距离
            distance = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
            turtle.write(distance)
            turtle.exitonclick()


        if __name__ == "__main__":
            locate()


---
## ***2022.07.04 DAY4***
### **1. 基本内置数据类型2**
#### **1. 布尔值**
- Python2中没有布尔值，直接用数字0表示False,1表示True。
- Python3中，把True和False定义成了关键字，但他们的本质还是0和1，可以和数字相加。

- 比较运算符
    - "==" 等于 相等：True,不相等：False
    - "!=" 不等于 不相等：True,相等：False
    - "<" 小于 小于：True,else：False
    - ">" 大于 大于：True,else：False
    - "<=" 小于等于 小于等于：True,else：False
    - ">=" 大于等于 大于等于：True,else：False

- 逻辑运算符
    - "or" 逻辑或 格式：x or y <=> x为True,返回True；x为False，返回y。
    - "and" 逻辑与 格式：x and y <=> x为True,返回y；x为False，返回False。
    - "not" 逻辑非 格式：not x <=> x为True,返回False；x为False，返回True。


- 同一运算符
    - 用于比较两个对象的存储单元，实际比较的是对象的地址。
    - is 判断两个标识符是不是引用同一个对象。
    - is not 判断两个标识符是不是引用不同对象。
    - is与"=="的区别：
        - is 判断两个标识符是不是引用同一个对象,即比较对象的地址。
        - == 用判断引用变量引用对象的值是否相等，默认调用对象的__eq__()方法。
    - 整数缓存问题
        - python仅仅对比较小的整数对象进行缓存（范围：[-5, 256]）缓存起来，而并非是所有的整数对象。而在Pycharm或者保存的文件执行，结果是不一样的，这是因为解释器做了部分优化（范围是[-5, 任意正整数]）。

#### **2. 字符串**
- 基础
    - 字符串的本质：字符序列。
    - Python的字符串是不可变的。我们无法对原字符串进行修改。可以将字符串的一部分复制到新创建的字符串，达到看似修改的效果。
    - 单字符也是作为一个字符串定义。
- 编码
    - Python3支持Unicode[65536] (ASCII[256]),表示世界上任何书面语言的字符。Python3的字符默认就是16位Unicode编码，ASCII码是Unicode编码的子集。
    - 使用函数ord()可以把字符转换成对应的Unicode码。
    - 使用函数chr()可以把十进制数字转换成对应的字符。

            # hello string
            def test(myWords):
                print(myWords)


            def test2():
                print(f"ord('A') = {ord('A')}")
                print(f"chr(72) = {chr(72)}")
                print(f"ord('霞') = {ord('霞')}")


            # Main
            if __name__ == '__main__':
                # test("I love you but you don't have any feelings.")
                test2()

- 引号创建字符串
    - 可以通过'' or "" 创建字符串。
    - 连续三个单引号或三个双引号，可以帮助我们创建多行字符串

            def test3():
                myWords1 = 'You are my only one.'
                print(myWords1)
                myWords2 = "Love you love your cat."
                print(myWords2)
                myWords3 = '''
                name = "YJP" 
                address = "B222"
                age = 21
                lover = "X" '''
                print(myWords3)


            # Main
            if __name__ == '__main__':
                test3()

- 空字符串和len()函数
    - Python允许空字符串的存在，即不包含任何字符。
    - len()用于计算字符串的长度。

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


            # Main
            if __name__ == '__main__':
                test3()

- 转义字符
    - 使用"\+特殊字符"。实现某些难以用字符表示的效果。
    - 常见转义字符：
        - \(在结尾时) 续行符
        - \\ 反斜杠
        - \' 单引号
        - \" 双引号
        - \b 退格（Backspace）
        - \n 换行
        - \t 横向制表符
        - \r 回车

                # 转义字符
                def test4():
                    myWords1 = '\twhat\'s up!\n'
                    myWords2 = "\t\"今宵绝胜无人共，\n\
                \t 卧看星河尽意明。\"\n"
                    print(myWords1)
                    print(myWords2)


                # Main
                if __name__ == '__main__':
                    test4()

- 字符串拼接
    - 可以使用+将多个字符串拼接起来。
        - 若 + 两边都是字符串，则拼接；
        - 若 + 两边都是数字，则加法运算；
        - 若 + 两边类型不同，则抛出异常。
    - 可以将多个字符串放在一起直接拼接。中间加空格。

            # 字符串拼接
            def test5():
                myWords1 = 'Noting is important.'
                myWords2 = 'If you leave.'
                print(myWords1 + myWords2)
                print('If you leave.' 'Noting is important.')


            # Main
            if __name__ == '__main__':
                test5()

- 字符串复制
    - 使用*可以实现字符串自由复制。
    -  myWords = 'I Love You\n'*10000

- 不换行打印
    - 调用print时，会自动打印一个换行符。
    - 若不想换行，可以通过参数end = "任意字符串"，实现末尾添加任何内容。

            # 不换行打印
            def test6():
                myWords1 = 'Noting is important but you.'
                print(myWords1, end="\n")
                myWords2 = 'I stand there.'
                print(myWords2, end="")


            # Main
            if __name__ == '__main__':
                test6()

- 从控制台读取字符串
    - 使用input()从控制台读取输入的内容。

            # 输入数据
            def test7():
                youWords = input("请输入你的回答：")
                print("Ok. Get it.")


            # Main
            if __name__ == '__main__':
                test7()

---
## ***2022.07.05 DAY5***
### **1. 字符串基础**
#### **1. str()实现数字转型字符串**
- str()可以帮助我们将其他数据类型转换成字符串。

        # str() 数字转字符串
        def test():
            a = 520
            print(f"a = {a}")
            aToString = str(a)
            print(f"aToString = {aToString}")


        # Main
        if __name__ == '__main__':
            test()

#### **2. 使用[]提取字符**
- 在字符串后面添加[] ,[]里边是指定的偏移量，可以提取带位置的单个字符。
- 正向搜索
    - 字符从0至len(str)-1进行编号。
- 反向搜索
    - 尾部到头从-1到-len(str)进行编号。

            # []提取字符
            def test2():
                myWords = "I Love You."
                print(myWords)
                print(f"myWords[0] = {myWords[0]}")
                print(f"myWords[len(myWords) - 1] = {myWords[len(myWords) - 1]}")
                print(f"myWords[-1] = {myWords[-1]}")
                print(f"myWords[-len(myWords)] = {myWords[-len(myWords)]}")


            # Main
            if __name__ == '__main__':
                test2()


#### **3. replace()实现字符串替换**
- 字符串是“不可改变”的。
- 需要替换某些字符。这时，只能通过创建新的字符串实现。
- 要改变原来的字符串，需要a = a.replace(...)
- str.replace(old,new,max) # 将str中的old换成new，最多换max次

        # replace()字符串替换
        def test3():
            myWords = "I Love You."
            print(f"myWords = {myWords}")
            newWords = myWords.replace("You", "Moon and stars")
            print(f"newWords = {newWords}")


        # Main
        if __name__ == '__main__':
            test3()

#### **4. 字符串切片slice操作**
- 切片slice操作可以让我们快速地提取子字符串。
- 标准格式为：[起始偏移量start : 终止偏移量end : 步长step]

- 典型操作(三个量为正数的情况)如下：
    - [:] 提取整个字符串
    - [start:] 从start索引开始到结尾
    - [:end] 从头开始直到end-1
    - [start:end] 从start到end-1
    - [start:end:step] 从start提取到end-1,步长step
- 操作数为负数
    - [-3:] 倒数三个
    - [-8:-3] 倒数第八个到倒数第三个(包头不包尾)
    - [::-1] 步长为负，从右到左反向提取

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


            # Main
            if __name__ == '__main__':
                test4()

- 起始偏移量和终止偏移量不在[0,len(str)-1]内，也不会报错。
- 起始偏移量小于0则会当成0，终止偏移量大于len(str)-1会被当成-1。

#### **5. split()分割和join()合并**
- split()可以基于指定分隔符将字符串分隔成多个子字符串(存储到列表中)。如果不指定分隔符，则默认使用空白字符(换行符/空格/制表符)。示例代码如下。

        # split()分隔
        def test5():
            myWords = "I Love You."
            print(f"myWords.split() = {myWords.split()}")
            print(f"myWords.split('Love') = {myWords.split('Love')}")


        # Main
        if __name__ == '__main__':
            test5()

- join()的作用和split()作用刚好相反，用于将一系列子字符串连接起来。
- 格式 : ''.join(a)

        # join()合并
        def test6():
            myWords = ['I love you.', 'But,', 'love is broken.']
            print(f"''.join(myWords) = {''.join(myWords)}")


        # Main
        if __name__ == '__main__':
            test6()

- join()比+的性能更好。join只生成一个对象，而+会生成多个对象。

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
            cmp()

#### **6. 字符串驻留机制和字符串比较**
- 字符串驻留
    - 仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串驻留池中。
    - Python支持字符串驻留机制，对于符合标识符规则的字符串会启用字符串驻留机制。
    - 仅包含下划线_、字母和数字。
- 如果 a = "a_b" , b = "a_b" , 则a is b 为True。
- is/not is 比较 id , ==/!= 比较 value。

#### **7. 成员操作符**
- in/not in 判断某个关键字(子字符串)是否存在于字符串中。

---
## ***2022.07.06 DAY6***
### **1. 字符串常用方法汇总**
#### 1. 查找方法
- len(a) 字符串长度
- a.startswith("开头字符串") 是否指定字符串开头
- a.endswith("结尾字符串") 是否指定字符串结尾
- a.find("查找字符串") 第一次出现指定字符串的位置
- a.rfind("查找字符串") 最后一次出现指定字符串的位置
- a.count("words") words出现的次数
- a.isalnum() 所有字符全是字母或数字

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


        # Main
        if __name__ == '__main__':
            test()

#### 2. 去除首尾信息
- 可以使用strip()去除字符串 [首] [尾] 指定信息。
- 使用lstrip()去除字符串[左边]指定信息。
- 使用rstrip()去除字符串[右边]指定信息。

        # 去除首尾信息
        def test2():
            myWords = "---只愿君心似我心，定不负相思意。---"
            print(f"\nmyWords = {myWords}")
            print(f"myWords.strip('-') = {myWords.strip('-')}")
            print(f"myWords.lstrip('-') = {myWords.lstrip('-')}")
            print(f"myWords.rstrip('-') = {myWords.rstrip('-')}")


        # Main
        if __name__ == '__main__':
            test2()

#### 3. 大小写转换
- a.capitalize() 产生新的字符串，句子首字母大写，即标准化。
- a.title() 产生新的字符串，每个单词首字母大写。
- a.upper() 产生新的字符串，所有字母转成大写。
- a.lower() 产生新的字符串，所有字母转成小写。
- a.swapcase() 产生新的字符串，所有字母大小写转换。

        # 大小写转换
        def test3():
            myWords = "you are my only one."
            print(f"\nmyWords = {myWords}")
            print(f"myWords.capitalize() = {myWords.capitalize()}")
            print(f"myWords.title() = {myWords.title()}")
            print(f"myWords.upper() = {myWords.upper()}")
            print(f"myWords.lower() = {myWords.lower()}")
            print(f"myWords.swapcase() = {myWords.swapcase()}")


        # Main
        if __name__ == '__main__':
            test3()

#### 4. 格式排版
- center()居中 , ljust()左对齐 , rjust()右对齐。
- 这三个函数用于对字符串实现排版。

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
            test4()

#### 5. 其它函数
- isalnum() 是否全是[字母]或[数字]
- isalpha() 检测字符串是否只由字母组成(含汉字,unicode)
- isdigit() 检测字符串是否只由数字组成(小数点也不算)
- isspace() 检测是否为空白符(空格/制表符/换行符)
- isupper() 是否为大写字母
- islower() 是否为小写字母


---
## ***2022.07.07 DAY7***
### **1. 字符串的格式化**
#### 1. format()基本用法
- 格式化字符串函数str.format()
- 可以通过{索引}/{参数名}，直接映射参数值，实现对字符串的格式化。

        # format()基本用法
        def test():
            info1 = "名字：{0}，年龄：{1}。"
            print(info1.format("YJP", 20))

            info2 = "名字：{0}，年龄：{1}。{0}学习Python。"
            print(info2.format("YJP", 20))

            info3 = "名字：{name}，年龄：{age}。"
            print(info3.format(name='YJP', age=20))


        # Main
        if __name__ == '__main__':
            test()

#### 2. 填充和对齐
- 填充和对齐一起使用
- ^、<、>分别是居中、左对齐、右对齐，后面带宽度。
- :号后面带填充的字符，只能是一个字符，默认用空格填充。

        # 填充和对齐
        def test2():
            print("{:*>8}".format("520"))
            print("我是{0},我喜欢数字{1:*<8}".format("YJP", "520"))


        # Main
        if __name__ == '__main__':
            test2()

#### 3. 数字的格式化
- 浮点数通用f,整数通过d进行需要的格式化。

        # 数字格式化
        def test3():
            str1 = "3.1415926格式化为{0:.2f}"
            print(str1.format(3.1415926))


        # Main
        if __name__ == '__main__':
            test3()

- 3.1415926 {:.2f} 3.14 保留小数点后两位
- 3.1415926 {:+.2f} 3.14 带符号保留小数点后两位
- 2.7114525 {:.0f} 3 不带小数，四舍五入
- 5 {:0>2d} 05 数字补0（填充左边，宽度为2）
- 5 {:x<4d} 5xxx 数字补x（填充右边，宽度为4）
- 10 {:x<4d} 10xx 数字补x（填充右边，宽度为4）
- 1000000 {:,} 1,000,000 以逗号分隔的数字格式
- 0.25 {:.2%} 25.00% 百分比格式
- 1000000000 {:.2e} 1.00E+09 指数记法
- 13 {:10d} --------13 右对齐（默认，宽度为10）
- 13 {:<10d} 13-------- 左对齐（宽度为10）
- 13 {:^10d} ----13---- 中间对齐（宽度为10）


#### 4. 可变字符串
- 在Python中，字符串属于不可变对象，不支持原地修改。如果需要修改其中的值，只能创建新的字符串对象。
- 但是，通常情况我们需要原地修改字符串，可以使用io.StingIO对象或array模块。

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
            test4()

---
## ***2022.07.08 DAY8***
### **1. 运算符**
#### 1. 基本运算符
- and， or， not 
    - 布尔与，布尔或，布尔非
- is, is not 
    - 判断是否为同一对象
- <, <= ,> , >=, ==, != 
    - 比大小
- |，^, & 
    - 按位或，按位异或，按位与
- <<, >> 
    - 移位
- ~ 
    - 按位翻转
- +, -, *, /, //, % 
    - 加，减，乘，浮点除，整数除，取余
- ** 
    - 幂运算

-代码测试：

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

#### 2. 特殊运算
- *加法*
    - 数字相加 3 + 2 ==> 5
    - 字符串拼接 '5' + '2' + '0' ==> '520'
    - 列表、元素等合并 [10, 20, 30] + [5, 10, 100] ==> [10, 20, 30, 5, 10, 100]

- *乘法*
    - 数字相乘 3 * 2 ==> 5
    - 字符串复制 "520" * 3 ==> "520520520"
    - 列表、元素等复制 [10, 20, 30] * 3 ==> [10, 20, 30, 10, 20, 30, 10, 20, 30]

#### 3. 复合赋值运算符
- += a += b <=> a = a + b
- -= 
- *=
- /=
- //=
- %=
- **= 
- <<=
- \>>=
- &=
- |=
- ^=

#### 4. 运算符优先级
- **
- ~
- *， /， %， //
- +， -
- \>\>, <<
- &
- ^, |
- <=, <, >, >=
- ==, !=
- =, +=, -=, /=, //=, %=, *=, **=
- is, is not
- not or and
- 小括号组织
- 乘除优先加减
- 位运算/算术运算 > 比较运算符 > 赋值运算符 > 逻辑运算符 

---
## ***2022.07.09 DAY9***
### **1. 序列**
#### 1. 基本内容
- 序列是一种数据存储方式，用来存储一些列的数据。在内存中，序列就是一块用来存放多个值得连续的内存空间。
- 一个整数序列可以表示为[10, 20, 30, 40]

#### 2. 列表
- 用于存储任意数目，任意类型的数据集合。
- 列表中的元素可以各不相同，可以是任意类型，比如：
    - a = [10, 20, '520', True]

- 列表对象常用方法：
    - list.append(x) 添加元素 将元素x添加到列表list的尾部。
    - list.extend(olist) 添加元素 将列表olist的所有元素加到列表list的尾部。
    - list.insert(index, x) 在列表list指定位置index插入元素x。
    - list.remove(x) 在列表list中删除首次出现的指定元素x。
    - list.pop([index]) 删除并返回列表list指定为止index处的元素，默认是最后一个元素。
    - list.clear() 删除列表所有元素，并不是删除列表对象。
    - list.index(x) 返回第一个x的索引位置，若不存在x元素抛出异常。
    - list.count(x) 返回指定元素x在列表list中出现的次数。
    - len(list) 返回列表中包含元素的个数。
    - list.reverse() 所有元素原地翻转。
    - list.sort() 所有元素原地排序。
    - list.copy() 返回列表对象的浅拷贝。

#### 3. 列表的创建
- 基本语法[]创建
    - a = [10, 20, 30]
    - a = []  # 创建一个空的列表对象

- list()创建
    - 使用list()可以将任何可迭代的数据转化成列表。
    - a = list()  # 创建一个空的列表对象
    - a = list(range(10))
    - a = list("YJP")

- range()创建整数列表
    - range()可以帮助我们非常方便地创建整数列表，这在开发中极其有用。
    - 语法格式：range(start, end, step)
        - start参数：可选，表示起始数字，默认为0。
        - end参数：必选，表示结尾数字。
        - step参数：可选，表示步长，默认为1。
    - Python3中range()返回的是一个range对象，而不是一个列表。我们需要通过list()方法将其转换成列表对象。
    - 典型示例为：
        - list(range(3, 15, 2)) ==> [3, 5, 7, 9, 11, 13]
        - list(range(20, 15, -1)) ==> [20, 19, 18, 17, 16]

- 推导式生成列表
    - a = [x * 2 for x in range(5)]  # 循环创建多个元素
    - a = [x * 2 for x range(100) if x % 9 == 0]  # 通过if过滤元素


---
## ***2022.07.10 DAY10***
### **1. 列表元素的增加**
- 一般只在列表的尾部添加或删除元素。
- 中间操作涉及到元素的移动。

#### 1. append() 方法
- 在列表尾部添加元素

#### 2. + 方法
- 产生新的对象

#### 3. extend() 方法
- 将目标列表的所有元素添加到本列表的尾部，属于原地操作。
- 不创建新的列表对象。

#### 4. insert() 插入函数
- 指定位置插入新的元素。
- 插入位置后边的元素需要向后移动。
- 尽量避免使用。

#### 5. 乘法扩展
- 复制元素得到大量重复的内容。

#### 6. 测试代码：

    # 元素的添加和删除
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


    # Main
    if __name__ == '__main__':
        test()

### **2. 列表元素的删除**
- 数组的拷贝。

#### 1. del方法
- 删除列表指定位置的元素。

#### 2. pop()方法
- 删除并返回指定位置元素。
- 如果未指定位置则默认操作列表最后一个元素。

#### 3. remove()方法
- 删除首次出现的指定元素，不不存在则抛出异常。

#### 4. 测试代码：

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
        test2()

---
## ***2022.07.11 DAY11***
### **1. 列表**
#### 1. 切片操作
- 切片是Python中重要的操作，适用于列表、元组、字符串等等。
- 切片的格式：
    - [起始偏移量start : 终止偏移量end : 步长step]
    - 不查清省略时，省略第二个冒号，默认步长为1。

- 测试程序
        # 切片操作
        def test():
            num = [10, 20, 30, 40, 50, 60]

            print(num[1:3:1])
            print(num[1::2])
            print(num[1:4])
            print(num[-5:-1])
            print(num[::-1])  # 逆序


        # Main
        if __name__ == '__main__':
            test()

#### 2. 列表的遍历
- 循环遍历
        for obj in listObj:
            print(obj)
- 测试程序

        # 遍历操作
        def test1():
            num = [10, 20, 30, 40, 50, 60]
            for i in num:
                print(f"{i},", end='')


        # Main
        if __name__ == '__main__':
            test1()

#### 3. 列表排序
- 修改原列
- a.sort() 默认是升序排列
- a.sort(reverse=True) 降序排列
- 随机打乱 import random
- random.shuffle(a)  # 打乱程序

        # 排序函数
        def test3():
            num = [10, 20, 30, 40, 50, 60]
            for i in num:  # 遍历列表
                print(f"{i},", end='')
            print('')
            random.shuffle(num)  # 打乱数组
            for i in num:  # 遍历列表
                print(f"{i},", end='')
            print('')
            num.sort(reverse=True)
            for i in num:  # 遍历列表
                print(f"{i},", end='')
            print('')


        # Main
        if __name__ == '__main__':
            test3()

#### 4. 建新列表排序
- 可以通过内置函数sorted()进行排序，这个方法返回新列表，不对原列表做修改。

        a = [10, 20, 30, 40, 50, 60]
        a = sorted(a)  # 默认升序
        a = sorted(a, reverse=True)  # 降序排列

#### 5. reverse迭代器
- 内置函数reversed()不对原列表做任何修改，只是返回一个逆序排列的迭代器对象。

        a = [10, 20, 30, 40, 50, 60]
        c = a.reversed(a)
        list(c)

#### 6. max 和 min
- 返回列表中的最大值和最小值

        a = [10, 20, 30, 40, 50, 60]
        max = max(a)
        min = min(a)

#### 7. sum
- 对列表中所有元素进行求和，对非数值型列表运算则会报错。

        a = [10, 20, 30, 40, 50, 60]
        sum = sum(a)

### **1. 二维列表**
- 二维列表可以帮助我们存储二维、表格的数据。

        # 二维列表
        def test4():
            table = [
                ["PEI", 21, '北京'],
                ["XIA", 20, '北京'],
                ["XXX", 24, '北京'],
            ]
            print(table)
            # 列表的遍历
            for i in range(3):
                for j in range(3):
                    print(table[i][j], end='\t')
                print()  # 打印完一行后换行


        # Main
        if __name__ == '__main__':
            test4()


---
## ***2022.07.12 DAY12***
### **1. 元组 ZIP**
#### 1. 元组
- 元组的核心特点：不可变序列。
- 元组的访问和处理时间比列表快。
- 与整数和字符串一样，元组可以作为字典的键，列表则永远不能作为字典的键使用。
- 元组的元素访问和列表一样，只不过返回的仍然是元组。

        a = (20, 30, 40, 50)

- 列表关于排序的方法list.sorted()是修改原列表对象，元组没有改方法。如果要对元组排序，只能使用内置函数sorted(tupleObj),并产生新的 列表 对象。

        a = (20, 10, 40, 5)
        sorted(a)

#### 2. ZIP
- zip（列表1，列表2，...）将多个列表对应位置的元素组合成元组，并返回这个zip对象。

        a = [10, 20, 30]
        b = [40, 50, 60]
        c = [70, 80, 90]
        d = zip(a,b,c)

        >>> [(10, 20, 30),(40, 50, 60),(70, 80, 90)]

#### 3. 生成推导式创建元组
- 生成器推导式使用小括号。
- 生成器生成的是一个生成器对象。
- 可以将生成器对象转化成 列表 或者 元组。
- 可以使用生成器对象的__next__()方法进行遍历。
- 不管使用什么方式访问，元素访问结束之后，如果需要重新访问其中的元素，必须重新创建给生成器对象。

    s = (x * 2 for x in range(5))
    tuple(s)  # 变成元组 只能访问一次
    s = (x * 2 for x in range(5))
    s.__next__()  # 依次返回值
    s.__next__()
    s.__next__()
    s.__next__()
    s.__next__()

### **2. 字典**

#### 1. 字典基础
- 字典是“键值对”的无序可变序列，字典中的每个元素都是一个“键值对”，包含︰"键对象”和“值对象”。可以通过“键对象”实现快速获取、删除、更新对应的“值对象”。
- 列表中我们通过“下标数字”找到对应的对象。字典中通过“键对象”找到对应的“值对象”。“键”是任意的不可变数据，比如∶整数、浮点数、字符串、元组。但是∶列表、字典、集合这些可变对象，不能作为“键”。并且“键”不可重复。
- “值”可以是任意的数据，并且可重复。

- 一个典型的字典定义方式：

        a = {'name':'YJP','age':21,'job':'programmer'}
        # name为键，后边的为值
        # a.get('name')

#### 2. 字典的创建
- 通过{}、dict()来创建字典对象。

        # 通过{} 创建字典
        def test():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)
            print(myDictionary.get('name'))
            print(myDictionary.get('gae'))
            print(myDictionary.get('job'))


        # Main
        if __name__ == '__main__':
            test()

        - 通过zip来创建字典对象。

---
## ***2022.07.13 DAY13***
### **1. 字典元素的访问**
#### 1. 通过[键]获得"值"。
- 若键不存在，则抛出异常。

        # 通过[键]获得“值”
        def test():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            print(myDictionary['name'])
            print(myDictionary['age'])
            print(myDictionary['job'])


        # Main
        if __name__ == '__main__':
            test()

#### 2. 通过get()获得"值"。
- 若键不存在，则返回None。
- 也可以设定键不存在时默认返回的对象。推荐使用get()获取"值"对象。

        # 通过get()获得“值”
        def test2():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            print(myDictionary.get('name'))
            print(myDictionary.get('gae'))
            print(myDictionary.get('job'))


        # Main
        if __name__ == '__main__':
            test2()

#### 3. 列出所有的键值对。

        # 列出所有的键值对
        def test3():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            print(myDictionary.items())


        # Main
        if __name__ == '__main__':
            test3()

#### 4. 列出所有的键 列出所有的值。

        # 列出所有的键 列出所有的值
        def test4():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            print(myDictionary.keys())
            print(myDictionary.values())


        # Main
        if __name__ == '__main__':
            test4()

#### 5. len()键值对的个数。

        print(len(myDictionary))

#### 6. 检测一个"键"是否在字典中。

        print('name' in myDictionary)

### **2. 字典的添加、修改、删除**
#### 1. 给字典新增"键值对"。
- 如果"键"已存在，则覆盖旧的 键值对。
- 如果"键"不存在，则新增 键值对。

        # 添加 键值对
        def test5():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            myDictionary['love'] = 'STM32'
            myDictionary['job'] = 'Embedded'

            print(myDictionary)


        # Main
        if __name__ == '__main__':
            test5()

#### 2. 使用update()将新字典中的所有键值全部添加到旧字典对象上。
- 如果key有重复，则直接覆盖。

        # 使用update()
        def test6():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            herDictionary = {'name': 'XX', 'age': 20, 'job': 'Engineer'}
            print(myDictionary)

            myDictionary.update(herDictionary)

            print(myDictionary)


        # Main
        if __name__ == '__main__':
            test6()

#### 3. 删除 使用del() & clear() & pop()
- del() 删除指定键值对。
- clear() 删除所有的键值对。
- pop() 删除指定键值对，同时返回对应的"值对象"。

#### 4. popitem()
- 随机删除和返回该键值对。字典是"无序可变序列"，依次没有第一个元素、最后一个元素的概念。popitem弹出随机的项，因此字典并没有"最后的元素"或者其他有关顺序的概念。若想一个接一个地移除并处理项，这个方法就非常有效（因为不用首先获取价值的列表）。

        # 使用popitem()
        def test7():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            myDictionary.popitem()
            print(myDictionary)
            myDictionary.popitem()
            print(myDictionary)


        # Main
        if __name__ == '__main__':
            test7()

### **3. 序列解包**
- 序列解包可以用于元组、列表、字典。
- 序列解包可以让我们方便地对多个变量赋值。

        # 序列解包
        def test8():
            x, y, z = 10, 20, 30
            print(x)

            (a, b, c) = (40, 50, 60)
            print(b)

            [e, f, g] = [70, 80, 90]
            print(g)


        # Main
        if __name__ == '__main__':
            test8()

- 字典解包

        # 序列解包 字典
        def test9():
            myDictionary = {'name': 'YJP', 'age': 21, 'job': 'Engineer'}
            print(myDictionary)

            # 默认对 键 进行操作
            name, age, job = myDictionary
            print(name)

            # 对 键值 对进行操作
            name2, age2, job2 = myDictionary.items()
            print(name2)

            # 对 值 对进行操作
            name3, age3, job3 = myDictionary.values()
            print(name3)


        # Main
        if __name__ == '__main__':
            test9()

---
## ***2022.07.14 DAY14***
### **1. 实例**
#### 1. 表格

    # 创建表格
    def createTable():
        staff1 = {'name': 'YJP', 'age': 21, 'city': '北京', 'job': 'Engineer'}
        staff2 = {'name': 'XX', 'age': 20, 'city': '上海', 'job': 'Engineer'}
        staff3 = {'name': 'ZHJ', 'age': 26, 'city': '上海', 'job': 'AI'}
        table = [staff1, staff2, staff3]

        # 获得第二行的人的name
        print("获得第二行的人的name:")
        print(table[1].get('name'))

        # 打印表中所有的年龄
        print("打印表中所有的年龄:")
        for i in range(len(table)):  # i --> 0, 1, 2
            print(table[i].get('age'))

        # 打印表的所有数据
        print("打印表的所有数据:")
        for i in range(len(table)):
            print(table[i].get('name'), table[i].get('age'), table[i].get('city'), table[i].get('job'))


    # Main
    if __name__ == '__main__':
        createTable()

### **2. 字典核心底层原理**

#### 1. 字典对象的核心是散列表
- 散列表是一个稀疏数组(总是有空白元素的数组)，数组的每个单元叫做bucket。
- 每个bucket又有两个部分：一个是键对象的引用，一个是值对象的引用。
- 哈希函数 存 取

- 总结：
    1. 键必须可以散列。
        - 数字、字符串、元组，都是可散列的。
        - 自定义对象需要支持下面三点：
            - 支持hash函数；
            - 支持通过__eq__()方法检测相等性；
            - 若a==b为真，则hash(a)==hash(b)也为真。 
    2. 字典在内存中开销巨大，典型的空间换时间。
    3. 字典查询熟读很快。
    4. 往字典里面添加新建可能导致扩容，导致散列表中的次序变化。因此，不要在遍历字典的同时进行字典的修改。

### **3. 集合**
- 集合是无需可变，元素不能重复。实际上，集合底层是字典实现，集合的所有元素都是字典中的"键对象"，因此是不能重复且唯一的。

#### 1. 集合的创建和删除
- 使用{}创建集合毛病使用add()方法添加元素

        # 使用 {} 创建集合
        def test():
            mySet = {10, 20, 30}
            print(mySet)
            mySet.add(520)
            print(mySet)


        # Main
        if __name__ == '__main__':
            test()

- 使用set()，经列表、元组等可迭代对象转成集合。如果原来的数据存在重复，则值保留一个。

        # 使用 set() 创建集合
        def test2():
            a = ['a', 'b', 'c', 'd']
            mySet = set(a)
            print(mySet)


        # Main
        if __name__ == '__main__':
            test2()

- remove删除指定元素，clear()清空整个集合

        mySet = {10, 20, 30}
        mySet.remove(20)  # 删除指定元素
        mySet.clear()  # 清空

#### 2. 集合的相关操作
- Python对集合提供了并集、交集、差集等运算。

        # 集合的运算
        def test3():
            mySet = {'embedded', 'vue', 'nature', 'space'}
            print(mySet)
            herSet = {'web', 'vue', 'others'}
            print(herSet)

            # 并集
            print(mySet | herSet)
            print(mySet.union(herSet))

            # 交集
            print(mySet & herSet)
            print(mySet.intersection(herSet))

            # 差集
            print(mySet - herSet)
            print(mySet.difference(herSet))


        # Main
        if __name__ == '__main__':
            test3()


---
## ***2022.07.15 DAY15***
### **1.控制语句**
#### 1.PyCharm
- IED --> IDLE PyCharm wingIDE Eclipse IPython
- Create New Project
- 选择路径 - 项目命名

#### 2. 选择结构
- 选择结构通过判断条件是否成立，来决定执行哪一个分支。
- 单分支结构
    - if语句单分支结构的语法如下：

            if 条件表达式:
                语句/语句块
    
    - 条件表达式：可以是逻辑表达式、关系表达式、算术表达式等等。
    - 语句/语句块：可以是一条语句，也可以是多条语句。多条语句，缩进必须对齐一致。

    - 结果为False:False/0/0.0/None/空序列对象/空range对象/空迭代对象
    - 条件表达式中，不能有赋值操作符"="

- 代码测试：

        # 选择结构
        def test():
            while True:
                num = input("请输入一个数:")
                if int(num) == 0:
                    print('num == 0')
                    break  # 退出循环

                if int(num) < 0:
                    print('num < 0')
                if int(num) > 0:
                    print('num > 0')
                
            del num


        # Main
        if __name__ == '__main__':
            test()

- 双分支结构
    - if语句双分支结构的语法如下：

            if 条件表达式:
                语句/语句块1
            else:
                语句/语句块2

- 代码测试：

        # 双分支选择结构
        def test2():
            while True:
                num = input("请输入一个数:")
                if int(num) == 0:
                    print('num == 0')
                    break  # 退出循环

                if int(num) < 0:
                    print('num < 0')
                else:
                    print('num > 0')
            del num


        # Main
        if __name__ == '__main__':
            test2()

- 三元条件运算符
    - Python提供了三元运算符，用来在某些简单双分支赋值的情况。
    - 三元条件运算符语法的格式如下：
        - 条件为真时的值 if (条件表达式) else 条件为假时的值
    - 写法更简洁、易读。

代码测试：

        # 三元条件运算符
        def test3():
            while True:
                num = input("请输入一个数:")
                print(num if int(num) < 10 else "num > 10")

                if int(num) == 0:
                    print('退出循环')
                    break  # 退出循环
            del num


        # Main
        if __name__ == '__main__':
            test3()

- 多分支结构
    - 多分支结构的语法如下：

            if 条件表达式1:
                语句/语句块1
            elif 条件表达式2:
                语句/语句块2
            elif 条件表达式3:
                语句/语句块3

- 代码测试：

        # 多分支选择结构
        def test4():
            while True:
                score = input("请输入分数:")
                if int(score) < 0 or int(score) > 100:
                    print("退出查询")
                    break  # 退出循环

                elif int(score) < 60:
                    print('成绩不及格')
                elif int(score) < 70:
                    print('成绩及格')
                elif int(score) < 80:
                    print('成绩中等')
                elif int(score) < 90:
                    print('成绩良好')
                elif int(score) <= 100:
                    print('成绩优秀')

            del score


        # Main
        if __name__ == '__main__':
            test4()

- 选择结构嵌套
    - 控制好缩进量，决定代码的从属关系。
    - 选择结构嵌语法如下：
            
            if 条件表达式1:
                语句块1
                if 条件表达式2:
                    语句块2
                else
                    语句块3
            else
                if 条件表达式4:
                    语句块4

#### 3. 循环结构
- 重复执行一条或者多条语句。
- 符合条件，执行循环里边的语句，否则退出循环。

- while 循环
    - while 循环的语法格式如下：
        
            while 条件表达式：
                循环体语句

- for 循环
    - 通常用于可迭代对象的遍历。
    - for循环的语法格式如下:
        
            for 变量 in 可迭代对象:
                循环体语句

- 测试代码：

        # for 循环
        def test5():
            sum = 0
            for i in range(10):
                sum += i
            print(sum)

            for x in (10, 20, 30):
                print(x * 10)

            d = {'name': 'YJP', 'age': 21}
            for x in d:
                print(x)
            for x in d.keys():
                print(x)
            for x in d.values():
                print(x)


        # Main
        if __name__ == '__main__':
            test5()   
    
- range 对象
    - range对象是一个迭代器对象，用来产生指定范围的数字序列。
    - 格式为： range(start, end, step)
    - 生成的数值序列从start开始到end结束(不含end)。
    - 如果没有填写start，则默认从0开始，step是可选步长，默认为1。
    - 示例：
        - for i in range(10) -- 序列：0 1 2 3 4 5 6 7 8 9
        - for i in range(3, 10) -- 序列：3 4 5 6 7 8 9
        - for i in range(3, 10, 2) -- 序列：3 5 7 9
 
- 代码测试:

        # 100以内的奇偶数和
        def test6():
            sum_all = 0
            sum_odd = 0
            sum_even = 0
            for x in range(101):
                sum_all += x
                if x % 2 == 1:
                    sum_odd += x
                else:
                    sum_even += x

            print("0-100累加总和{0},奇数和{1}，偶数和{2}".format(sum_all, sum_odd, sum_even))


        # Main
        if __name__ == '__main__':
            test6()

---
## ***2022.07.16 DAY16***
### **1. 控制语句2**
#### 1. 嵌套循环
- 多重循环

- 代码测试1：

        # 嵌套循环
        def test():
            for i in range(5):
                for j in range(6):
                    print(f"{i} ", end='')
                print('')  # 换行


        # Main
        if __name__ == '__main__':
            test()


- 代码测试2：

        # 九九乘法表
        def test2():
            for i in range(1, 10):
                for j in range(1, i):
                    # print(f"{i}*{j}={i * j}", end='  ')
                    print("{0}*{1}={2}".format(i, j, i*j), end='  ')
                print("")


        # Main
        if __name__ == '__main__':
            test2()

- 代码测试3：

        # 表格
        def test3():
            staff1 = dict(name='高小一', age=20, salary=30000, city='北京')
            staff2 = dict(name='高小二', age=19, salary=20000, city='上海')
            staff3 = dict(name='高小幺', age=18, salary=10000, city='深圳')
            table = [staff1, staff2, staff3]

            for x in table:
                if x.get("salary") > 15000:
                    print(x)


        # Main
        if __name__ == '__main__':
            test3()

#### 2. break语句

- break语句用于while和for循环，用来结束整个循环。
- 当有嵌套循环时，break语句只能跳出最近一层的循环。

        while True:
            if 退出条件:
                break

#### 2. continue语句

- continue语句用于结束本次循环，继续下一次。
- 多个循环嵌套时，continue也是应用于最近的一层循环。

#### 3. else语句

- while, for 循环可以附带一个else语句(可选)。如果for,while语句没有被break语句结束，则会执行else字句，否则不执行。语法格式如下：

        while 条件表达式:
            循环体
        else:
            语句块

        for 变量 in 可迭代对象:
            循环体
        else:
            语句块

#### 4. 循环代码优化

- 三个原则提高代码的运行效率：
    - 尽量减少循环内部不必要的计算；
    - 嵌套循环中，尽量减少内层循环的计算；
    - 局部变量查询较快，尽量使用局部变量；

---
## ***2022.07.17 DAY17***
### **1. 使用zip()并行迭代**
- 通过zip()函数对多个序列进行并行迭代，zip()函数在最短序列"用完"时就会停止。
- 测试代码：

        # zip
        def test():
            names = ("First", "Second", "Third", "Fourth")
            ages = (28, 26, 20, 25)
            jobs = ("老师", "程序员", "学生", "公务员")

            for name, age, job in zip(names, ages, jobs):
                print("{0}--{1}--{2}".format(name, age, job))


        if __name__ == '__main__':
            test() 

- 执行结果：

        First--28--老师
        Second--26--程序员
        Third--20--学生
        Fourth--25--公务员

### **2. 推导式创建序列**

#### 1. 列表推导式
- 列表推导式生成列表对象，语法如下：
    1. [表达式 for item in 可迭代对象]
    2. [表达式 for item in 可迭代对象 if 条件判断]

- 代码测试：

        # 列表推导式
        def test2():
            a = [x for x in range(1, 5)]
            b = [x * 2 for x in range(1, 5)]
            c = [x * 5 for x in range(1, 20) if x % 5 == 0]

            print(a)
            print(b)
            print(c)


        if __name__ == '__main__':
            test2()

- 执行结果：

        [1, 2, 3, 4]
        [2, 4, 6, 8]
        [25, 50, 75]

#### 2. 字典推导式
- 字典推导式生成字典对象，格式如下：
    1. {key_expression : value_expression for 表达式 in 可迭代对象}
    2. 类似于列表推导式，字典推到也可以增加if条件判断、多个for循环。

- 代码测试：

        # 字典推导式
        def test3():
            # 统计文本中字符出现的次数
            myWords = "I Love You, File, Edit, All Right."
            char_count = {c: myWords.count(c) for c in myWords}
            print(myWords)
            print(char_count)


        if __name__ == '__main__':
            test3()

- 执行结果：

        I Love You, File, Edit, All Right.
        {'I': 1, ' ': 6, 'L': 1, 'o': 2, 'v': 1, 'e': 2, 'Y': 1, 'u': 1, ',': 3, 'F': 1, 'i': 3, 'l': 3, 'E': 1, 'd': 1, 't': 2, 'A': 1, 'R': 1, 'g': 1, 'h': 1, '.': 1}


#### 3. 集合推导式
- 集合推导式生成集合，和列表推导式的语法格式类似：
    1. [表达式 for item in 可迭代对象]
    2. [表达式 for item in 可迭代对象 if 条件判断]

- 代码测试：

        # 集合推导式
        def test4():
            a = {x for x in range(1, 100) if x % 9 == 0}
            print(a)


        if __name__ == '__main__':
            test4()

- 执行结果：

        {99, 36, 72, 9, 45, 81, 18, 54, 90, 27, 63}

#### 4. 生成器推导式(生成元组)
- 元组是没有推导式的。
- 一个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代发现数据已经没有了。

- 代码测试：

        # 生成器推导式 生成元组
        def test5():
            gnt = (x for x in range(1, 100) if x % 9 == 0)
            for x in gnt:
                print(x, end=' ')
            for x in gnt:
                print(x, end=' ')


        if __name__ == '__main__':
            test5()

- 执行结果：

        9 18 27 36 45 54 63 72 81 90 99 

---
## ***2022.07.18 DAY18***
### **1. 循环画图**
#### 1. 绘制同心圆
- 代码测试：

        # 绘制棋盘
        def test():
            myColor = ('green', 'yellow', 'blue', 'pink')
            t = turtle.Pen()
            t.width(10)  # 画笔宽度
            t.speed(0)  # 画笔速度
            for i in range(15):
                t.penup()
                t.goto(0, -i * 20)
                t.pendown()
                t.color(myColor[i % len(myColor)])
                t.circle(30 + i * 20)

            turtle.done()  # 程序执行完，窗口仍然在


        if __name__ == '__main__':
            test()

#### 2. 绘制棋盘
- 代码测试：

        # 绘制棋盘
        def test2():
            # myColor = ('green', 'yellow', 'blue', 'pink')
            width = 30
            num = 18

            x1 = [(-300, 300), (-300 + width * num, 300)]
            y1 = [(-300, 300), (-300, 300 - width * num)]

            t = turtle.Pen()
            t.width(2)  # 画笔宽度
            t.speed(10)  # 画笔速度

            for i in range(19):  # 竖线
                t.penup()
                # t.color(myColor[i % len(myColor)])
                t.goto(x1[0][0], x1[0][1] - 30 * i)
                t.pendown()
                t.goto(x1[1][0], x1[1][1] - 30 * i)

            for i in range(19):  # 横线
                t.penup()
                # t.color(myColor[i % len(myColor)])
                t.goto(y1[0][0] + 30 * i, y1[0][1])
                t.pendown()
                t.goto(y1[1][0] + 30 * i, y1[1][1])

            turtle.done()  # 程序执行完，窗口仍然在


        if __name__ == '__main__':
            test2()

---
## ***2022.07.19 DAY19***
### **1. 函数的用法和底层分析**
#### 1. 函数简介
- 一个程序由一个个任务组成；函数就是代表一个任务或者一个功能。
- 函数是代码复用的通用机制。

#### 2. Python函数的分类
- 内置函数
    - str()、list()、len()等,直接拿来使用。
- 标准库函数
    - import语句导入库，然后使用其中定义的函数。
- 第三方库函数
    - Python社区提供很多高质量的库。
- 用户自定义函数
    - 用户自己定义函数。

#### 3. Python函数的定义和调用
- 核心要点：

        def 函数名([参数列表]):
            "文档字符串"
            函数体/若干语句

- 要点：
    - 使用def来定义函数，然后一个空格和函数名称；
    - Python执行def时，会创建一个函数对象，并绑定到函数变量名上。
- 参数列表
    - 圆括号内是形式参数列表，有多个参数则用逗号隔开。
    - 形式参数不需要声明类型，也不需要指定函数返回值类型。
    - 无参数，也必须保留留空的圆括号。
    - 实参列表必须与形参列表一一对应。
- return 返回值
    - 函数体包含return语句，则结束函数执行并返回值。
    - 函数体不包含return语句，则返回None值。
- 调用函数之前，必须要先定义函数
    - 内置函数对象会自动创建
    - 标准库和第三方函数，通过import导入模块时，会执行模块中的def语句。

---
## ***2022.07.20 DAY20***
### **1. 函数的用法和底层分析**
#### 1. 形参和实参

    # 形参和实参
    def printMax(a, b):
        """ 实现两个数的比较，并返回较大的值 """
        if a > b:
            print(a, '较大值')
        elif a < b:
            print(b, '较大值')
        else:
            print("a, b一样大")


    if __name__ == '__main__':
        printMax(10, 20)
        printMax(30, 5)

#### 2. 文档字符串
- 程序的可读性最重要，一般建议在函数体开始的部分附上函数兴义说明，这就是文档字符串，也有人称为函数的注释。
- 通过三个单引号或者三个双引号类实现，中间可以加入多行文字进行说明。
- 调用help(函数名,__doc__)可以打印输出函数的文档字符串。

        def play():
            """ 快来找我玩啊 """
            print("快来找我玩啊!!!")


        if __name__ == '__main__':
            help(play.__doc__)
            play()


---
## ***2022.07.21 DAY21***
### **1. 函数的用法和底层分析**
#### 1. 函数的返回值
- 函数体包含return语句，则 结束函数执行 并 返回值。
- 函数体不包含return语句，则返回None值。
- 要返回多个返回值，使用列表、元组、字典、集合将多个值存起来。

        def add(a, b):
            """ 计算两个数[a 和 b]的和 """
            print("计算两个数的和：{0}，{1}，{2}".format(a, b, a+b))
            return a+b


        if __name__ == '__main__':
            c = add(30, 40)
            print("c = ", c)

- 返回多个值

        def test(x, y, z):
            """ 返回各自乘以10之后的值 """
            return [x*10, y*10, z*10]


        if __name__ == '__main__':
            print(test(1, 2, 3))

---
## ***2022.07.22 DAY22***
### **1. 函数的用法和底层分析**
#### 1. 内存分析
- Python中，一切皆是对象。
- 实际上，执行def定义函数后，系统就创建了相应的函数对象。

        def print_star(n):
            print("*"*n)

        print(print_star)
        print(id(print_star))
        c = print_star
        c(10)

#### 2. 变量的作用域（全局变量和局部变量）
- 变量起作用的范围叫做变量的作用域，不同作用域同名变量之间互不影响。
- 变量分为：全局变量、局部变量
- 全局变量
    - 在函数和类定义之外声明的变量。作用域为定义的模块，从定义位置开始直到模块结束。
    - 全局变量降低了函数的通用性和可读性。应尽量避免全局变量的使用。
    - 全局变量一般做常量使用。
    - 函数内要改变全局变量的值，使用global声明一下。
- 局部变量
    - 在函数体中(包含形式参数)声明的变量。
    - 局部变量的引用比全局变量快，优先考虑使用。
    - 如果局部变量和全局变量同名，则在函数内隐藏全局变量，只是用同名的局部变量。

            A = 100  # 全局变量


            def test():
                """变量的作用域"""
                global A  # 使用全局变量
                print(A)
                A = 300
                print(A)

                
                print(locals())  # 打印输出的局部变量
                print(globals())  # 打印输出的全局变量


            if __name__ == '__main__':
                test()
                print(A)

- 在特别强调效率的地产或循环次数较多的地方，可以通过将全局变量转化成局部变量提高运行速度。

---
## ***2022.08.08 DAY23***
### **1. 函数的用法和底层分析**
#### 1. 参数的传递
- Python中参数的传递都是“引用传递”。
- 具体操作可分为两类：
    - 对“可变对象”进行“写操作”，直接作用域原对象本身。
    - 对“不可变对象”进行“写操作”，会产生一个新的“对象空间”，并用新的值填充这块空间。

- 可变对象有:
    - 字典、列表、集合、自定义对象等
- 不可变对象有:
    - 数字、字符串、元组、function等

#### 2.传递不可变对象的引用
- 传递参数是不可变对象，实际传递还是对象的引用。在“复制操作”中，由于不可变对象无法修改，系统会新创建一个对象。

#### 3. 浅拷贝与深拷贝
- 内置函数copy(浅拷贝)、deepcopy(深拷贝)
- 浅拷贝：不拷贝子对象的内容，只拷贝子对象的引用。
- 深拷贝：会连子对象的内容全部拷贝一份，对子对象的修改不会影响源对象。

浅拷贝示例代码：

    import copy

    a_list = [20, 50, [5, 6]]
    b_list = copy.copy(a_list)

    def test():
        print("a : ", a_list)
        print("b : ", b_list)

        b_list.append(100)
        b_list[2].append(200)
        print("浅拷贝...")
        print("a : ", a_list)
        print("b : ", b_list)


    if __name__ == '__main__':
        test()

运行结果：

        a :  [20, 50, [5, 6]]
        b :  [20, 50, [5, 6]]
        浅拷贝...
        a :  [20, 50, [5, 6, 200]]
        b :  [20, 50, [5, 6, 200], 100]

深拷贝示例代码：

    import copy

    def test_deepcopy():
        a_list = [20, 50, [5, 6]]
        b_list = copy.deepcopy(a_list)

        print("a : ", a_list)
        print("b : ", b_list)

        b_list.append(100)
        b_list[2].append(200)
        print("深拷贝...")
        print("a : ", a_list)
        print("b : ", b_list)


    if __name__ == '__main__':
        test_deepcopy()

运行结果：

    a :  [20, 50, [5, 6]]
    b :  [20, 50, [5, 6]]
    深拷贝...
    a :  [20, 50, [5, 6]]
    b :  [20, 50, [5, 6, 200], 100]

#### 3.不可变对象含可变子对象
- 传递不可变对象（数字、字符串、元组、function）时，不可变对象里包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生了变化。

#### 4.参数的几种类型

- 位置参数
    - 函数调用时，实参默认按照顺序传递，需要个数和形参匹配。

- 默认值参数
    - 参数设置默认值，这样的参数在传递时就是可选的。
    - 默认值参数放在位置参数的后面。

- 命名参数
    - 可以按照形参的名称传递参数。

- 可变参数
    - 可变数量的参数
    - *param 将多个参数收集到一个“元组”对象中。
    - **param 将多个参数收集到一个“字典”对象中。

- 强制命名参数
    - 可变参数后面新增新的参数，必须是“强制命名参数”。

---
## ***2022.08.09 DAY25***
### **1. lambda表达式和匿名函数**
- lambda表达式可以用来声明匿名函数。
- lambda函数是一种简单的、在同一行中定义函数的方法。
- lambda函数实际生成了一个函数对象。
- lambda表达式只允许包含一个表达式，不能包含复杂语句，该表达式的计算结果就是函数的返回值。
- lambda表达式的基本语法如下：
    - lambda arg1, arg3, arg3 ... : <表达式>
    - arg1...为函数的参数。<表达式>相当于函数体。运算结果是：表达式的运算结果。

示例：

    def test_lambda():
        """ lambda表达式 """
        f = lambda a, b, c : a + b + c
        print(f)
        print(f(2, 3, 4))

        g = [lambda a:a*2, lambda b:b*3, lambda c:c*4]
        print(g[0](6), g[1](7), g[2](8))


    if __name__ == '__main__':
        test_lambda()

结果：

    <function test_lambda.<locals>.<lambda> at 0x000001A59415F160>
    9
    12 21 32

---
## ***2022.08.10 DAY26***
### **1. 函数基础**
#### 1. eval()函数
- 将字符串str作为有效的表达式来求值并返回计算结果。
- 语法：
    - eval(source[ , globals[ , locals]]) -> value
- 参数：
    - source:一个python表达式或函数compile返回的代码对象。
    - globals:可选。必须是dictionary。
    - locas:可选。任意映像对象。

示例：

    def test_eval():
        str = "print('string')"
        eval(str)

        a = 10
        b = 20
        c = eval("a+b")
        print("c = {0}".format(c))

    if __name__ == '__main__':
        test_eval()

结果：

    string
    c = 30

#### 2. 递归函数
- 自己调用自己
- 终止条件
    - 表示递归什么时候结束。一般用于返回值，不再调用自己。
- 递归步骤
    - 把第n步的值和n-1步相关联。

示例：

    def test_01(n):
        """ 递归函数 """
        print("*test01,n = ", n)
        if(n == 0):
            print("over...")
        else:
            test_01(n - 1);
        print("*test01,n = ", n)


    if __name__ == '__main__':
        test_01(5)

结果：

    *test01,n =  5
    *test01,n =  4
    *test01,n =  3
    *test01,n =  2
    *test01,n =  1
    *test01,n =  0
    over...
    *test01,n =  0
    *test01,n =  1
    *test01,n =  2
    *test01,n =  3
    *test01,n =  4
    *test01,n =  5

递归算阶乘：

    def factorial(number):
        """ 递归算阶乘 """
        if number == 1:
            return 1;
        else:
            return number * factorial(number - 1);


    if __name__ == '__main__':
        print("5! = {0}".format(factorial(5)))

结果：

    5! = 120

#### 3. 嵌套函数(内部函数)

- 嵌套函数：在函数内部定义的函数
- 使用说明：
    - 封装 - 数据隐藏
        - 外部无法访问'嵌套函数'
    - DRY
        - 可以让函数内部避免重复代码
    - 闭包

示例：

    def test_02():
        """ 嵌套函数 """
        print('outer running')

        def inner01():
            """ 只能内部可用 """
            print('inner01 running')

        inner01()


    if __name__ == '__main__':
        test_02()

结果：

    outer running
    inner01 running

#### 4. nonlocal 关键字

- nonlocal 用来声明外层的局部变量
- global 用来声明全局变量

示例：

    def outer():
        b = 10

        def inner():
            nonlocal b  # 声明外部函数的局部变量
            print("inner b:",b)
            b = 20

        inner()
        print("outer b:", b)


    if __name__ == '__main__':
        outer()

结果:

    inner b: 10
    outer b: 20

#### 5. LEGB规则
- Python在查找名称时,是按照LEGB规则查找的：
- Local --> Enclosed --> Global --> Built in
- Local 函数或者类的方法内部
- Enclosed 嵌套函数
- Global 模块中的全局变量
- Built in Python为自己保留的特殊名称

测试LEGB：

    str = "global"
    def outer():
        str = "outer"

        def inner():
            str = "inner"
            print(str)

        inner()

    outer()

---
## ***2022.08.11 DAY27***

### **第六章 面向对象编程**
- Python完全采用了面向对象的思想，是真正面向对象的编程语言，完全支持面向对象的基本功能，例如：继承、多态、封装等。
- Python中，一切皆对象。

#### **面向对象和面向过程区别**
- 面向过程编程 --> 关注程序的逻辑流程 --> 小规模程序
- 面向对象编程 --> 设计者 --> 大规模程序

#### **对象的进化**
- 问题越来越复杂...
- 编程语言本身也在进化...
- 数据类型越来越复杂... 
- 简单数据 -> 数组 -> 结构体 -> 对象

#### **类的定义**
- 通过类定义数据类型的属性(数据)和方法(行为)
- 类也称为类对象，类的实例也被称为实例对象。
- 定义类的语法格式如下：

        class 类名:
            类体
- 要点：
    - 类名必须符合标识符的规则。首字母大写，多个单词使用驼峰原则。
    - 类名中可以定义属性和方法。
    - 属性用来描述数据，方法用来描述这些数据相关的操作。

实例：

    class Student:  # 类名首字母大写，多个单词驼峰原则

        def __init__(self, name, score):  # self必须位于第一个参数
            """ 构造函数 """
            self.name = name
            self.score = score

        def get_score(self):  # self必须位于第一个参数
            """ 获取分数信息 """
            print("{0}的分数为{1}".format(self.name, self.score))
            return self.score


    def test():
        student1 = Student("YJP", 99)  # 调用构造函数
        student1.get_score()


    if __name__ == '__main__':
        test()

结果：

    YJP的分数为99

#### **构造函数__init__()**
- \__init__(self)方法：初始化创建好的对象。初始化指的是："给实例对象赋值"。
- \__new__()方法：用于创建对象，但我们一般无需从定义该方法，
- self可以自定义，但必须是init的第一个参数。


#### **实例属性**
- 实例属性是从属实例对象的属性，也称为实例变量。
- 要点：
    - 实例属性一般在__init__()方法中通过如下代码定义：
        - self.实例属性名 = 初始值
    - 在本类的其他实例方法中，也是通过self进行访问：
        - self.实例属性名
    - 创建实例对象后，通过实例对象访问：
        - obj01 = 类名()  # 创建对象，调用__init__()初始化属性
        - obj02.实例属性名 = 值  # 可以给已有属性赋值，也可以新加属性

#### **实例方法**
- 实例方法是从属于实例对象的方法。
- 实例方法的定义格式：

        def 方法名(self [形参列表])
            函数体

- 方法的调用格式如下：
    - 对象.方法名([实参列表])
- 要点：
    - 定义实例方法时，第一个参数必须是self。和面的一样，self指当前的实例对象。
    - 调用实例方法时，不需要也不能给self传参。self由解释器自动传参。

- 其他操作
    - dir(obj)可以获得对象的所有属性、方法。
    - obj.\__dict__ 对象的属性字典。
    - pass 空语句
    - isinstance(对象，类型) 判断“对象”是不是“指定类型”

---
## ***2022.08.12 DAY28***

#### **类对象**

- 类对象

        class Student:
            pass  # 空语句

- type 模具类

实例：

    class Student:  # 类名首字母大写，多个单词驼峰原则

        def __init__(self, name, score):  # self必须位于第一个参数
            """ 构造函数 """
            self.name = name
            self.score = score

        def get_score(self):  # self必须位于第一个参数
            """ 获取分数信息 """
            print("{0}的分数为{1}".format(self.name, self.score))
            return self.score


    def test():
        Stu = Student
        s1 = Student("YJP", 99)
        s2 = Stu("XX", 100)
        s1.get_score()
        s2.get_score()


    if __name__ == '__main__':
        test()

结果：

    YJP的分数为99
    XX的分数为100

#### **类属性**

- 类属性是属于“类对象”的属性，也称为“类变量”。由于类属性也属于类对象，可以被所有的实例对象共享。
- 类属性的定义方法：

        class 类名:
            类变量名 = 初始值

- 在类中或者类的外面，我们可以通过:类名.类变量名 来读写。

实例：

    class People:

        company = "Embedded"  # 类属性
        count = 0  # 类属性

        def __init__(self, name, age, score):
            self.name = name  # 实例属性
            self.age = age
            self.score = score
            People.count += 1

        def get_info(self):  # 实例方法
            print("------------------------------")
            print("- name    : {0}".format(self.name))
            print("- age     : {0}".format(self.age))
            print("- score   : {0}".format(self.score))
            print("- company : {0}".format(self.company))
            print("- count   : {0}".format(self.count))
            print("------------------------------")


    def test2():
        p1 = People("YJP", 21, 99)
        p1.get_info()

    if __name__ == '__main__':
        test2()

结果：

    ------------------------------
    - name    : YJP
    - age     : 21
    - score   : 99
    - company : Embedded
    - count   : 1
    ------------------------------

#### **类方法**

- 类方法是从属于“类对象”的方法。
- 类方法通过装饰器@classmethod来定义，格式如下：
        
        @classmethod
        def 类方法名(cls, [形参列表]):
            函数体

- 要点：
    - @classmethod必须位于方法上面的第一行。
    - 第一个cls必须要有，cls指的就是类对象本身。
    - 调用格式：类名.类方法名(参数列表)
    - 类方法中访问实例属性和实例方法会导致错误。
    - 子继承父类方法时，传入cls是子类对象。

实例：

    class Human:
        base = "碳基生命体"  # 类属性

        @classmethod
        def get_base(cls):
            print(cls.base)


    if __name__ == '__main__':
        Human.get_base()

结果：

    碳基生命体

#### **静态方法**

- Python中允许定义与类对象无关的方法，称为静态方法。
- 静态方法和模块中定义普通函没用区别，只不过静态方法放到了类的名字空间里面，需要通过类调用。
- 静态方法通过装饰器@staticmethon来定义，格式如下：

        @staticmethod
        def 类方法名([形参列表]):
            函数体

- 要点：
    - @staticmethod必须位于方法上面的第一行。
    - 第一个cls必须要有，cls指的就是类对象本身。
    - 调用格式：类名.静态方法名(参数列表)
    - 静态方法中访问实例属性和实例方法会导致错误。

实例：

    class Human:
        base = "碳基生命体"  # 类属性

        @classmethod  # 类方法
        def get_base(cls):
            """ 打印信息 """
            print(cls.base)

        @staticmethod
        def add(number1, number2):  # 静态方法
            """ 加法计算 """
            sum = number1 + number2
            print("计算:S{0} + {1} = {2}".format(number1, number2, sum))
            return sum


    if __name__ == '__main__':
        Human.get_base()
        Human.add(45, 55)

结果：

    碳基生命体
    计算:S45 + 55 = 100


---
## ***2022.08.13 DAY29***

#### **\__del__方法(析构函数)和垃圾回收机制**

- \__del__方法称为"析构方法"，用于实现对象被销毁时所需要的操作。比如：释放对象占用的资源。
- Python实现自动的垃圾回收，当对象没有被引用时（引用计数为0），由垃圾回收器调用\__del__方法。
- 我们使用del语句删除对象，从而保证调用了\__del__方法。
- 系统会自动调用\__del__方法，一般不需要自定义析构方法。

实例：

    # 析构函数
    class Person:

        def __del__(self):
            print("销毁对象：{0}".format(self))

    if __name__ == "__main__":
        p1 = Person()
        p2 = Person()
        del p2
        print("程序结束")

结果：

    销毁对象：<__main__.Person object at 0x000001E1E3C51D00>
    程序结束
    销毁对象：<__main__.Person object at 0x000001E1E3BD8400>


#### **\__call__方法**

- 定义了\__call__方法的对象，称为“可调用对象”，即该对象可以像调用函数一样去调用。

实例:

    # 测试可调用方法__call__()
    class SalaryAccount():
        """ 工资计算类 """

        def __call__(self, salary):
            print("算工资了:")
            yourSalary = salary * 12
            daySalary = salary // 22.5
            hourSalary = salary // 8

            return dict(yourSalary = yourSalary, monthSalary = salary, daySalary = hourSalary)


    def test2():
        s = SalaryAccount()
        print(s(3000))


    if __name__ == "__main__":
        test2()

结果：

    算工资了:
    {'yourSalary': 36000, 'monthSalary': 3000, 'daySalary': 375}

#### **方法没有重载**

- 在其他语言中，可以定义多个重名的方法。
- Python中，方法的参数没有类型（调用时确定参数的类型），参数的数量也可以由可变参数控制。因此，Python中没有方式是重载的。
- 定义一个方法即有多种调用方式，相当于实现了其他语言中的方法的重载。
- 定义多个重名的方法，只有最后一个有效。

---
## ***2022.08.14 DAY30***

#### **私有属性和私有方法**
- Python对于类的成员没有严格的访问控制限制，这是其与其他面向对象语言有区别。
- 私有方法和私有属性要点：
    - 通常我们约定，两个下划线开头的属性是私有的(private)。其他为公共的(public)。
    - 类内部可以访问私有属性(方法)。
    - 类外内部不能直接访问私有属性(方法)。
    - 类外部可以通过"\__类名__私有属性(方法)名"访问私有属性方法。

实例：

    # 测试私有属性
    class Employee:

        __company = "百战程序员"  # 类变量

        def __init__(self, name, age, score):
            self.name = name
            self.age = age  # 私有属性
            self.__score = score

        def __work(self):  # 私有方法
            print("{0}要好好工作".format(self.name))
            print("年龄:{0}".format(self.age))
            print("公司:{0}".format(self.__company))


    def test():
        e = Employee("YJP", 21, 99)
        print(e.name)
        print(e.age)
        print(e._Employee__score)
        # print(dir(e))

        e._Employee__work()
        print(Employee._Employee__company)


    if __name__ == "__main__":
        test()

结果：

    YJP
    21
    99
    YJP要好好工作
    年龄:21
    公司:百战程序员
    百战程序员

#### **@property装饰器_get和set方法**
- @property可以将一个方法的调用方式变成“属性调用”。

实例:

    # 测试私有属性
    class Employee:

        __company = "百战程序员"  # 类变量

        def __init__(self, name, age, salary):
            self.name = name
            self.age = age  # 私有属性
            self.__salary = salary

        def __work(self):  # 私有方法
            print("{0}要好好工作".format(self.name))
            print("年龄:{0}".format(self.age))
            print("公司:{0}".format(self.__company))

        # 测试@property的最简化使用
        @property
        def salary(self):
            print("salary run...")
            return self.__salary

        @salary.setter
        def salary(self, salary):
            if 1000 < salary < 50000:
                self.__salary = salary
            else:
                print("录入错误！薪水在1000--50000的范围内。")



    def test():
        e = Employee("YJP", 21, 3000)
        print(e.name)
        print(e.age)
        print(e._Employee__salary)
        # print(dir(e))

        e._Employee__work()
        print(Employee._Employee__company)

        print(e.salary)
        e.salary = -2000
        print(e.salary)
        e.salary = 40000
        print(e.salary)


    if __name__ == "__main__":
        test()

结果:

    YJP
    21
    3000
    YJP要好好工作
    年龄:21
    公司:百战程序员
    百战程序员
    salary run...
    3000
    录入错误！薪水在1000--50000的范围内。
    salary run...
    3000
    salary run...
    40000

---
## ***2022.08.15 DAY31***

### **面向对象三大特征**

#### **封装**
- 隐藏对象的属性和实现方法，只对外提供必要的方法。

#### **继承**
- 继承可以让子类具有父类的特性，提高代码的重用性
- 子类继承父类（基类）
- python支持多重继承，一个子类可以继承多个父类。
- 语法格式：

        class 子类类名(父类1[, 父类2, ...]):
            类体

- 如果在类定义中没有指定父类，则默认父类为object类。也就是说，object是所有类的父类，里面定义了所有类的公有的默认实现，比如：\__new__()。
- 定义子类时，必须在其构造函数中调用父类的构造函数。调用格式如下：

        父类名.__init__(self, 参数列表)

实例：

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def get_info(self):
            print(self.name, "的年龄为：", self.age)


    class Student(Person):

        def __init__(self, name, age, score):
            Person.__init__(self, name, age)  # 必须显式调用父类的初始化方法，不然解释器不会去调用
            self.score = score

        def get_info(self):
            print(self.name, "的年龄为：", self.age, "分数为：", self.score)


    def test():
        s = Student("YJP", 21, 149)
        s.get_info()
        print(dir(s))


    if __name__ == "__main__":
        test()

运行结果：

    YJP 的年龄为： 21 分数为： 149
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'get_info', 'name', 'score']

- 成员继承：子类继承了父类除构造方法之外的所有成员。
- 方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类的方法，也称为重写。

重写案列：

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def introduce_name(self):
            print("我的名字为：", self.name)

        def introduce_age(self):
            print("我的年龄为：{0}".format(self.age))


    class Student(Person):

        def __init__(self, name, age, score):
            Person.__init__(self, name, age)  # 必须显式调用父类的初始化方法，不然解释器不会去调用
            self.score = score

        def introduce_name(self):
            """ 重写父类的方法 """
            print("大家好，我的名字为：", self.name)

        def introduce_age(self):
            """ 重写父类的方法 """
            print("大家好，我的年龄为：{0}".format(self.age))


    def test():
        s = Student("YJP", 21, 149)
        s.introduce_name()
        s.introduce_age()


    if __name__ == "__main__":
        test()

运行结果：

    大家好，我的名字为： YJP
    大家好，我的年龄为：21

---
## ***2022.08.16 DAY32***

**重写\__str__()方法**

- object有一个\__str__()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮助我们查看对象的信息。
- \__str__()可以重写。

代码示例：

    class Person:  # 默认继承object类
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return "名字是{0}，年龄为{1}".format(self.name, self.age)


    def test():
        p = Person("YJP", 21)
        print(p)


    if __name__ == "__main__":
        test()

运行结果：

    名字是YJP，年龄为21

**多重继承**
- Python支持多重继承，一个子类可以有多个“直接父类”。这样，就具备了“多个父类的特点”。
- 类的整体层次结构会异常复杂，尽量避免使用。

**MRO()**
- Python支持多继承，在父类中有相同名字的方法，在子类中没有定义父类名时，解释器将从左到右按顺序搜索。
- MRO(Method Resolution Order):方法解释顺序。
- 通过MRO()方法获得“类的层次结构”，方法解释顺序也是按照“类的层次顺序”寻找的。

**super()获得父类定义**
- 子类通过super()获取父类的方法。
- super()代表父类的定义，不是父类对象。

代码示例：

    class A:

        def say(self):
            print("A:", self)


    class B(A):

        def say(self):
            # A.say(self)
            super().say()
            print("B:", self)


    def test():
        B().say()


    if __name__ == "__main__":
        test()

运行结果：

    A: <__main__.B object at 0x000001465ED01D00>
    B: <__main__.B object at 0x000001465ED01D00>

---
## ***2022.08.17 DAY33***

#### **多态**
- 多态是指同一个方法调用由于对象不同会产生不同的行为。
- 多态是方法的多态，属性没有多态。
- 多态的存在是有2个必要条件：继承、方法重写。

代码示例：

    class Man:

        def eat(self):
            print('饿饿,饭饭...')

    class Chinese(Man):

        def eat(self):
            print('中国人用筷子吃饭')

    class English(Man):

        def eat(self):
            print('英国人用叉子吃饭')

    class Indian(Man):

        def eat(self):
            print('印度人用手吃饭饭')

    def manEat(m):
        if isinstance(m, Man):
            m.eat()
        else:
            print("不能吃饭...")


    def test():
        manEat(Man())
        manEat(Chinese())
        manEat(English())
        manEat(Indian())


    if __name__ == "__main__":
        test()

运行结果：

    饿饿,饭饭...
    中国人用筷子吃饭
    英国人用叉子吃饭
    印度人用手吃饭饭

#### **特殊方法和运算符的重载**
- Python的运算符实际上是通过调用对象的特殊方法实现的。
        
        + --- __add__
        - --- __sub__
        <, >=, == --- __it__, __le__, __eq__ 
        >, >=, != --- __gt__, __ge__, __ne__
        |, ^, & ----- __or__, __xor__, __and__
        <<, >> ------ __lshift__, __rshift__
        *, / -------- __mul__, __truediv__ 
        %, // ------- __mod__, __floordiv__
        ** ---------- __pow__

- 常见的特殊方法

        __init__    构造方法
        __del__     析构方法
        __repr__, __str__   打印,转换
        __call__    函数调用
        __getattr__ 点号调用
        __setattr__ 属性赋值
        __getitem__ 索引运算
        __setitem__ 索引赋值
        __len__     长度

实例：

    class Person:
        def __init__(self, name):
            self.name = name

        def __add__(self, other):
            if isinstance(other, Person):
                return "{0}--{1}".format(self.name, other.name)
            else:
                return "不是同类对象，故不能相加。"

    def test():
        P1 = Person("YJP")
        P2 = Person("XX")
        x = P1 + P2
        print(x)


    if __name__ == "__main__":
        test()

结果：

    YJP--XX

---
## ***2022.08.18 DAY34***

#### **特殊属性**
- Python对象中包含了很多双下滑线开始和结束的属性，这些是特殊属性，有特殊用法。

        obj.__dict__    对象属性字典
        obj.__class__   对象所属的类
        class.__bases__ 类的基本元祖（多继承）
        class.__base__  类的基类
        class.__mro__   类层次结构
        class.__subclasses__()  子类列表

#### **对象的浅拷贝和深拷贝**
- 变量的赋值操作
    - 只是形成两个变量，实际还是指向同样一个对象，
- 浅拷贝
    - Python中的拷贝一般都是浅拷贝。
    - 浅拷贝，对象包含的子对象内容不拷贝。所以，源对象和拷贝对象都会引用同一个子对象。
- 深拷贝
    - 使用copy模块的deepcope函数，递归拷贝对象中包含的子对象。源对象和拷贝对象所有的子对象也不同。

测试代码：

    import copy

    class MobilePhone:
        def __init__(self, cpu, screen):
            self.cpu = cpu
            self.screen = screen

    class CPU:
        def calculate(self):
            print("算你个！@#￥%……&*")
            print("CPU对象:", self)

    class Screen:
        def show(self):
            print("显示一个好看的画面，亮瞎你的钛合金大眼")
            print("Screen对象:", self)

    def test():
        c1 = CPU()
        c2 = c1
        print(c1)
        print(c2)

        s1 = Screen()
        m1 = MobilePhone(c1, s1)
        m2 = copy.copy(m1)
        print(m1)
        print(m1.cpu)
        print(m1.screen)

        print(m2)
        print(m2.cpu)
        print(m2.screen)

        m3 = copy.deepcopy(m1)
        print(m3)
        print(m3.cpu)
        print(m3.screen)


    if __name__ == "__main__":
        test()

运行结果：

    <__main__.CPU object at 0x000001A235B88400>
    <__main__.CPU object at 0x000001A235B88400>

    <__main__.MobilePhone object at 0x000001A235B72340>
    <__main__.CPU object at 0x000001A235B88400>
    <__main__.Screen object at 0x000001A235C01D00>

    <__main__.MobilePhone object at 0x000001A235C97FD0>
    <__main__.CPU object at 0x000001A235B88400>
    <__main__.Screen object at 0x000001A235C01D00>

    <__main__.MobilePhone object at 0x000001A235CA5430>
    <__main__.CPU object at 0x000001A235CE1AC0>
    <__main__.Screen object at 0x000001A235CE1B50>



#### **组合**
- 实现一个类拥有另一个类的方法和属性。

测试代码：

    # 测试组合

    class A1:
        def say_a1(self):
            print("a1:", self)

    class B1:
        def __init__(self, a):
            self.a = a

    def test():
        a1 = A1()
        b1 = B1(a1)
        b1.a.say_a1()


    if __name__ == "__main__":
        test()

运行结果:

    a1: <__main__.A1 object at 0x0000024CFE288400>

---
## ***2022.08.19 DAY35***

#### **设计模式_工厂模式实现**
- 实现创建者和使用者的分离。

测试代码:

    class Benz:
        pass

    class BMW:
        pass

    class BYD:
        pass

    class CarFactory:
        def create_car(self, brand):
            if brand == "奔驰":
                return Benz()
            elif brand == "宝马":
                return BMW()
            elif brand == "比亚迪":
                return BYD()
            else:
                return "未知品牌，无法创建"

    def test():
        factory = CarFactory()
        c1 = factory.create_car("奔驰")
        c2 = factory.create_car("宝马")
        c3 = factory.create_car("比亚迪")
        print(c1)
        print(c2)
        print(c3)


    if __name__ == "__main__":
        test()

运行结果:

    <__main__.Benz object at 0x0000024F64232340>
    <__main__.BMW object at 0x0000024F642325E0>
    <__main__.BYD object at 0x0000024F64357610>

#### **单例模式**
- 核心作用就是确保一个类只有一个实例，并且提供一个访问该实例的全局访问点。
- 减少对系统资源的开销。

测试代码：

    class MySimgleton:

        __obj = None  # 类属性
        __init_flag = True

        def __new__(cls, *args, **kwargs):
            if cls.__obj == None:
                cls.__obj = object.__new__(cls)

            return cls.__obj

        def __init__(self, name):
            if MySimgleton.__init_flag:
                print("init......")
                self.name = name
                MySimgleton.__init_flag = False

    def test():
        a = MySimgleton("aa")
        b = MySimgleton("bb")
        print(a)
        print(b)
        c = MySimgleton("cc")
        print(c)


    if __name__ == "__main__":
        test()

运行结果；

    init......
    <__main__.MySimgleton object at 0x000001E8376A7DC0>
    <__main__.MySimgleton object at 0x000001E8376A7DC0>
    <__main__.MySimgleton object at 0x000001E8376A7DC0>

---
## ***2022.08.20 DAY36***

#### **模块**
- 只要是以.py为后缀的文件，都可以称为模块。
- 模块中包含：
    - 变量
    - 函数
    - class 面向对象(类->对象)
    - 可执行代码

- 模块的好处就是管理方便。

