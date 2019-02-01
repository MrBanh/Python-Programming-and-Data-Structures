"""
(Turtle: draw four circles)
Write a program that draws four circles in the center of the screen
"""
import turtle

turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.circle(50)

turtle.done()
