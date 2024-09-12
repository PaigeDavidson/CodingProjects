# Paige Davidson
# CS1400 - MO1
# Assignment 1B

import turtle
#first circle
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#second circle
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()

#third circle
turtle.penup()
turtle.goto(0, 75)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()

#eyes
turtle.penup()
turtle.goto(-15, 125)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(15, 125)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#mouth
turtle.penup()
turtle.goto(-15, 105)
turtle.pendown()
turtle.color("pink")
turtle.width(10)
turtle.setheading(340)
turtle.circle(45, 45)

#buttons
turtle.penup()
turtle.goto(0, 40)
turtle.pendown()
turtle.color("orange")
turtle.width(1)
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
#2
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
#3
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#arms
turtle.penup()
turtle.goto(65, 30)
turtle.pendown()
turtle.width(7)
turtle.color("brown")
turtle.goto(120, 75)
turtle.goto(125, 95)
turtle.goto(120, 75)
turtle.goto(125, 55)
turtle.goto(120, 75)
turtle.goto(130, 75)
#2
turtle.penup()
turtle.goto(-65, 30)
turtle.pendown()
turtle.goto(-120, 75)
turtle.goto(-125, 95)
turtle.goto(-120, 75)
turtle.goto(-125, 55)
turtle.goto(-120, 75)
turtle.goto(-130, 75)

#hat
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.color("red")
turtle.width(2)
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(40, 150)
turtle.goto(40, 170)
turtle.goto(20, 170)
turtle.goto(20, 200)
turtle.goto(-20, 200)
turtle.goto(-20, 170)
turtle.goto(-40, 170)
turtle.goto(-40, 150)
turtle.goto(0, 150)
turtle.end_fill()


#end
turtle.hideturtle()
turtle.done()
