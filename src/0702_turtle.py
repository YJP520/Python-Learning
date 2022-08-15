#
# 2022/07/02 Python Learning
#
# 图形化界面学习 turtle
#

import turtle  # 导入turtle模块


# 图形化界面学习 turtle
def turtle_study():
    turtle.showturtle()  # 显示箭头
    turtle.write("YJP")  # 写字符串
    turtle.forward(300)  # 前继300像素
    turtle.color("red")  # 画笔颜色改成红色
    turtle.left(90)  # 箭头左转90度
    turtle.forward(300)
    turtle.goto(0, 50)  # 去坐标(0,50) 会划线
    turtle.goto(0, 0)  # 去坐标(0,0)
    turtle.penup()  # 抬笔 不划线
    turtle.goto(0, 300)  # 去坐标(0,300)
    turtle.goto(0, 0)  # 去坐标(0,0)
    turtle.pendown()  # 放笔 画线
    turtle.goto(0, 50)  # 去坐标(0,50)
    turtle.goto(50, 0)  # 去坐标(50,0)
    turtle.circle(100)  # 画圆 半径100


# 奥运五环
def OlympicFiveCircles():
    turtle.width(10)  # 画笔宽度

    turtle.color("blue")  # 画笔颜色
    turtle.circle(50)  # 画圆1

    turtle.penup()  # 抬笔 不划线
    turtle.goto(120, 0)  # 移动
    turtle.pendown()  # 放笔 画线
    turtle.color("black")  # 画笔颜色改成红色
    turtle.circle(50)  # 画圆2

    turtle.penup()  # 抬笔 不划线
    turtle.goto(240, 0)  # 移动
    turtle.pendown()  # 放笔 画线
    turtle.color("red")  # 画笔颜色改成红色
    turtle.circle(50)  # 画圆3

    turtle.penup()  # 抬笔 不划线
    turtle.goto(60, -50)  # 移动
    turtle.pendown()  # 放笔 画线
    turtle.color("yellow")  # 画笔颜色改成红色
    turtle.circle(50)  # 画圆4

    turtle.penup()  # 抬笔 不划线
    turtle.goto(180, -50)  # 移动
    turtle.pendown()  # 放笔 画线
    turtle.color("green")  # 画笔颜色改成红色
    turtle.circle(50)  # 画圆5


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # turtle_study()
    OlympicFiveCircles()
