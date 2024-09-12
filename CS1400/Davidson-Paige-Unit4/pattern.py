# Paige Davidson
# CS1400 - MO1
# Assignment ??

import turtle
import random

def reset():
    turtle.reset()
    turtle.speed(0)


def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    iteration = 360 / count
    for i in range(count):
        setRandomColor()
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left(iteration * i)
        turtle.forward(offset)
        turtle.left(rotation)
        turtle.pendown()
        drawRectangle(width, height)
        turtle.hideturtle()


def drawRectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

def drawCirclePattern(centerX, centerY, offset, radius, count):
    iteration = 360 / count
    for i in range(count):
        setRandomColor()
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.left(iteration)
        turtle.forward(radius + offset)
        turtle.pendown()
        turtle.circle(radius)
        turtle.hideturtle()


def drawSuperPattern(num=3):
    for i in range(num):
        # circle pattern variables
        number = random.randint(1, 2)
        centerX = random.randint(-400, 400)
        centerY = random.randint(-400, 400)
        offset = random.randint(0, 200)
        radius = random.randint(0, 200)
        count = random.randint(0, 200)
        # rectangle pattern variables
        width = random.randint(1, 500)
        height = random.randint(1, 500)
        rotation = random.randint(0, 360)
        if number % 2 == 0:
            drawCirclePattern(centerX, centerY, offset, radius, count)
        else:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        turtle.hideturtle()

def setRandomColor():
    color = random.randint(1, 4)
    if color == 1:
        color = "purple"
    elif color == 2:
        color = "blue"
    elif color == 3:
        color = "orange"
    else:
        color = "green"
    turtle.color(color)


def done():
    turtle.hideturtle()
    turtle.done()
