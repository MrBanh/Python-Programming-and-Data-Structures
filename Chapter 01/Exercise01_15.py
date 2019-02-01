"""
(Turtle: draw two triangles)
Write a program that draws two triangles
"""
import turtle


for i in range(3):
    turtle.right(60)
    turtle.forward(50)
    turtle.right(60)

for i in range(3):
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)

turtle.done()