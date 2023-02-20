import turtle
from random import randrange

tao = turtle.Turtle()
color = ["black","red","SpringGreen",
"MediumSlateBlue","Aquamarine","Gray","Wheat"]


tao.circle(150)
tao.left(90)
tao.penup()
tao.forward(300)

for x in range(5):
    for i in range(5) :
        tao.left(144)
        tao.pendown()
        tao.color(color[randrange(6)])
        tao.forward(150)
    tao.color(color[randrange(6)])

    tao.penup()
    tao.left(144)
    tao.forward(300)

tao.done()
