#
# 2022/07/18 Python Learning
#
# 绘制棋盘
#

# import random
# import turtle
# import time
# import math
# import this  # print(this.v)

import turtle


# 绘制同心圆
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
    # test()
    test2()
