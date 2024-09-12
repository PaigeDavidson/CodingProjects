# Paige Davidson
# CS1400 - MO1
# Assignment practice

import turtle
from random import randint

turtle.speed(100)

# color change


def color1():
    a = randint(0, 5)
    if a == 1:
        return "skyblue"
    elif a == 2:
        return "light salmon"
    elif a == 3:
        return "gold"
    elif a == 4:
        return "cyan"
    else:
        return "pink"

# angle change


def angle():
    num = randint(10, 360)
    return num

# circle size


def size():
    num = randint(10, 100)
    return num

# placement change


def place():
    a = randint(-250, 250)
    b = randint(-250, 250)
    return a, b

# flower loop


for j in range(5):
    turtle.penup()
    turtle.color(color1())
    turtle.goto(place())
    for i in range(35):
        turtle.pendown()
        turtle.circle(size())
        turtle.right(angle())

turtle.hideturtle()
turtle.done()
