"""
(Turtle: draw four squares)
Write a program that draws four squares in the
center of the screen
"""
import turtle

for i in range(4):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

turtle.done()