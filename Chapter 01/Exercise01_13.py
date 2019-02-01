"""
Turtle: draw a cross)
Write a program that draws a cross
"""
import turtle

# Draw the horizontal line
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.forward(200)

# Draw the vertical line
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.right(90)
turtle.forward(200)

turtle.done()
