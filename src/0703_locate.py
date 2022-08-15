#
# 2022/07/03 Python Learning
#
# 定义多点坐标，绘出折线，计算起始点和终点的距离
#

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
