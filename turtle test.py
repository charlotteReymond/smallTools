import turtle
from random import random

wn = turtle.Screen()
wn.setup(800,800)
#wn.bgcolor("black")

turtle.colormode(255)
turtle.pensize(10)
turtle.ht()

turtle.color(0,0,255)

for i in range(100):
    turtle.penup()
    x=random()
    y=random()
    turtle.goto(800*x-400,800*y-400)
    turtle.pendown()
    turtle.forward(1)
    

