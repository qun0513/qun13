'''
import numpy as np
a=np.array([0.99,0.789,0.45])#数组
print(a)
b=[0.99,0.789,"兰大"]#列表
print(b)
c=(45.88,99,0.98)#元组
print(c)
d=np.random.randn(4,5)
print(d)
e=d.reshape(5,4)
print(e)
'''
import turtle

turtle.title('Python（冰墩墩）') #可以自己修改名称
turtle.speed(40)  # 可以自己调节速度
# 左手
turtle.penup()

turtle.goto(177, 112)

turtle.pencolor("lightgray")

turtle.pensize(3)

turtle.fillcolor("white")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(80)

turtle.circle(-45, 200)

turtle.circle(-300, 23)

turtle.end_fill()

# 左手内
turtle.penup()

turtle.goto(182, 95)

turtle.pencolor("black")

turtle.pensize(1)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.setheading(95)

turtle.pendown()

turtle.circle(-37, 160)

turtle.circle(-20, 50)

turtle.circle(-200, 30)

turtle.end_fill()

# 轮廓
# 头顶
turtle.penup()

turtle.goto(-73, 230)

turtle.pencolor("lightgray")

turtle.pensize(3)

turtle.fillcolor("white")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(20)

turtle.circle(-250, 35)

# 左耳
turtle.setheading(50)

turtle.circle(-42, 180)

# 左侧
turtle.setheading(-50)

turtle.circle(-190, 30)

turtle.circle(-320, 45)

# 左腿
turtle.circle(120, 30)

turtle.circle(200, 12)

turtle.circle(-18, 85)

turtle.circle(-180, 23)

turtle.circle(-20, 110)

turtle.circle(15, 115)

turtle.circle(100, 12)

# 右腿
turtle.circle(15, 120)

turtle.circle(-15, 110)

turtle.circle(-150, 30)

turtle.circle(-15, 70)

turtle.circle(-150, 10)

turtle.circle(200, 35)

turtle.circle(-150, 20)

# 右手
turtle.setheading(-120)

turtle.circle(50, 30)

turtle.circle(-35, 200)

turtle.circle(-300, 23)

# 右侧
turtle.setheading(86)

turtle.circle(-300, 26)

# 右耳
turtle.setheading(122)

turtle.circle(-53, 160)

turtle.end_fill()



# 右耳内
turtle.penup()

turtle.goto(-130, 180)

turtle.pencolor("black")

turtle.pensize(1)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(120)

turtle.circle(-28, 160)

turtle.setheading(210)

turtle.circle(150, 20)

turtle.end_fill()



# 左耳内
turtle.penup()

turtle.goto(90, 230)

turtle.setheading(40)

turtle.begin_fill()

turtle.pendown()

turtle.circle(-30, 170)

turtle.setheading(125)

turtle.circle(150, 23)

turtle.end_fill()



# 右手内
turtle.penup()

turtle.goto(-180, -55)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.setheading(-120)

turtle.pendown()

turtle.circle(50, 30)

turtle.circle(-27, 200)

turtle.circle(-300, 20)

turtle.setheading(-90)

turtle.circle(300, 14)

turtle.end_fill()



# 左腿内
turtle.penup()

turtle.goto(108, -168)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(-115)

turtle.circle(110, 15)

turtle.circle(200, 10)

turtle.circle(-18, 80)

turtle.circle(-180, 13)

turtle.circle(-20, 90)

turtle.circle(15, 60)

turtle.setheading(42)

turtle.circle(-200, 29)

turtle.end_fill()

# 右腿内
turtle.penup()

turtle.goto(-38, -210)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(-155)

turtle.circle(15, 100)

turtle.circle(-10, 110)

turtle.circle(-100, 30)

turtle.circle(-15, 65)

turtle.circle(-100, 10)

turtle.circle(200, 15)

turtle.setheading(-14)

turtle.circle(-200, 27)

turtle.end_fill()



# 右眼
# 眼圈
turtle.penup()

turtle.goto(-64, 120)

turtle.begin_fill()

turtle.pendown()

turtle.setheading(40)

turtle.circle(-35, 152)

turtle.circle(-100, 50)

turtle.circle(-35, 130)

turtle.circle(-100, 50)

turtle.end_fill()

# 眼珠
turtle.penup()

turtle.goto(-47, 55)

turtle.fillcolor("white")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(25, 360)

turtle.end_fill()

turtle.penup()

turtle.goto(-45, 62)

turtle.pencolor("darkslategray")

turtle.fillcolor("darkslategray")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(19, 360)

turtle.end_fill()

turtle.penup()

turtle.goto(-45, 68)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(10, 360)

turtle.end_fill()

turtle.penup()

turtle.goto(-47, 86)

turtle.pencolor("white")

turtle.fillcolor("white")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(5, 360)

turtle.end_fill()



# 左眼
# 眼圈
turtle.penup()

turtle.goto(51, 82)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(120)

turtle.circle(-32, 152)

turtle.circle(-100, 55)

turtle.circle(-25, 120)

turtle.circle(-120, 45)

turtle.end_fill()

# 眼珠
turtle.penup()

turtle.goto(79, 60)

turtle.fillcolor("white")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(24, 360)

turtle.end_fill()

turtle.penup()

turtle.goto(79, 64)

turtle.pencolor("darkslategray")

turtle.fillcolor("darkslategray")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(19, 360)

turtle.end_fill()

turtle.penup()

turtle.goto(79, 70)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(10, 360)

turtle.end_fill()

turtle.penup()

turtle.goto(79, 88)

turtle.pencolor("white")

turtle.fillcolor("white")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(0)

turtle.circle(5, 360)

turtle.end_fill()



# 鼻子
turtle.penup()

turtle.goto(37, 80)

turtle.fillcolor("black")

turtle.begin_fill()

turtle.pendown()

turtle.circle(-8, 130)

turtle.circle(-22, 100)

turtle.circle(-8, 130)

turtle.end_fill()



# 嘴
turtle.penup()

turtle.goto(-15, 48)

turtle.setheading(-36)

turtle.begin_fill()

turtle.pendown()

turtle.circle(60, 70)

turtle.setheading(-132)

turtle.circle(-45, 100)

turtle.end_fill()



# 彩虹圈
turtle.penup()

turtle.goto(-135, 120)

turtle.pensize(5)

turtle.pencolor("cyan")

turtle.pendown()

turtle.setheading(60)

turtle.circle(-165, 150)

turtle.circle(-130, 78)

turtle.circle(-250, 30)

turtle.circle(-138, 105)

turtle.penup()

turtle.goto(-131, 116)

turtle.pencolor("slateblue")

turtle.pendown()

turtle.setheading(60)

turtle.circle(-160, 144)

turtle.circle(-120, 78)

turtle.circle(-242, 30)

turtle.circle(-135, 105)

turtle.penup()

turtle.goto(-127, 112)

turtle.pencolor("orangered")

turtle.pendown()

turtle.setheading(60)

turtle.circle(-155, 136)

turtle.circle(-116, 86)

turtle.circle(-220, 30)

turtle.circle(-134, 103)

turtle.penup()

turtle.goto(-123, 108)

turtle.pencolor("gold")

turtle.pendown()

turtle.setheading(60)

turtle.circle(-150, 136)

turtle.circle(-104, 86)

turtle.circle(-220, 30)

turtle.circle(-126, 102)

turtle.penup()

turtle.goto(-120, 104)

turtle.pencolor("greenyellow")

turtle.pendown()

turtle.setheading(60)

turtle.circle(-145, 136)

turtle.circle(-90, 83)

turtle.circle(-220, 30)

turtle.circle(-120, 100)

turtle.penup()



# 爱心
turtle.penup()

turtle.goto(220, 115)

turtle.pencolor("brown")

turtle.pensize(1)

turtle.fillcolor("brown")

turtle.begin_fill()

turtle.pendown()

turtle.setheading(36)

turtle.circle(-8, 180)

turtle.circle(-60, 24)

turtle.setheading(110)

turtle.circle(-60, 24)

turtle.circle(-8, 180)

turtle.end_fill()



# 五环
turtle.penup()

turtle.goto(-5, -170)

turtle.pendown()

turtle.pencolor("blue")

turtle.circle(6)

turtle.penup()

turtle.goto(10, -170)

turtle.pendown()

turtle.pencolor("black")

turtle.circle(6)

turtle.penup()

turtle.goto(25, -170)

turtle.pendown()

turtle.pencolor("brown")

turtle.circle(6)

turtle.penup()

turtle.goto(2, -175)

turtle.pendown()

turtle.pencolor("lightgoldenrod")

turtle.circle(6)

turtle.penup()

turtle.goto(16, -175)

turtle.pendown()

turtle.pencolor("green")

turtle.circle(6)

turtle.penup()



turtle.pencolor("black")

turtle.goto(-16, -160)

turtle.write("BEIJING 2022", font=('Arial', 10, 'bold italic'))

turtle.hideturtle()


#自定义内容，会显示在图片上方一行文字
turtle.pencolor("black")

turtle.goto(-96, 260)

turtle.write("我和你", font=('新宋体', 20, 'bold italic')) #调整文案，字体，字号

turtle.hideturtle()



turtle.done()


import matplotlib.pyplot as plt
