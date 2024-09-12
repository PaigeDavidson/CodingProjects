# Paige Davidson
# CS1400 - MO1
# Assignment 2
import turtle
xPos = eval(input("Enter x Coordinate: "))
yPos = eval(input("Enter y Coordinate: "))
diameter = eval(input("Enter Bullseye Diameter: "))
radius = int(diameter / 2)

# outside circle
radius *= 4
turtle.penup()
yPos -= radius
turtle.goto(xPos, yPos)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

# 3nd circle
yPos += ((1/4) * radius)
radius *= (3/4)
turtle.penup()
turtle.goto(xPos, yPos)
turtle.pendown()
turtle.fillcolor("blue")
turtle.color("blue")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

# 2nd circle
yPos += ((1/3) * radius)
radius *= (2/3)
turtle.penup()
turtle.goto(xPos, yPos)
turtle.pendown()
turtle.fillcolor("red")
turtle.color("red")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

# bulls eye
yPos += ((1/2) * radius)
radius = int(diameter / 2)
turtle.penup()
turtle.goto(xPos, yPos)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

# end code
turtle.hideturtle()
turtle.done()
