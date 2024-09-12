# Paige Davidson
# CS1400 - MO1
# Assignment ??

import turtle


def drawChessboard(startX, startY, width=250, height=250):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.color("black")
    turtle.goto(startX + width, startY)
    turtle.goto(startX + width, startY + height)
    turtle.goto(startX, startY + height)
    turtle.goto(startX, startY)
    drawAllRectangles(startX, startY, width, height)
    turtle.hideturtle()
    turtle.done()


def drawAllRectangles(startX, startY, width, height):
    xPosition = startX
    yPosition = startY
    for j in range(4):
        for i in range(4):
            drawRectangle(xPosition, yPosition, width/8, height/8)
            xPosition += width / 4
        xPosition = startX
        yPosition += height / 4

    xPosition = startX + width / 8
    yPosition = startY + height / 8
    for j in range(4):
        for i in range(4):
            drawRectangle(xPosition, yPosition, width/8, height/8)
            xPosition += width / 4
        xPosition = startX + width / 8
        yPosition += height / 4


def drawRectangle(x, y, rectangleWidth, rectangleHeight):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.goto(x + rectangleWidth, y)
    turtle.goto(x + rectangleWidth, y + rectangleHeight)
    turtle.goto(x, y + rectangleHeight)
    turtle.goto(x, y)
    turtle.end_fill()

