import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(0)
tim.hideturtle()

colors = [(202, 164, 109), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41),
          (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72)]


def move():
    for i in range(10):
        tim.color(random.choice(colors))
        tim.up()
        tim.dot(30)
        tim.forward(50)


y_value = 0
for i in range(10):
    move()
    y_value += 50
    tim.setposition(0, y_value)

screen = Screen()
screen.exitonclick()
