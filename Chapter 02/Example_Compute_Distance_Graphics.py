# Example_Compute_Distance_Graphics.py - Calculates the distance between 2 points and
# graphs it using turtle module.

import turtle

# Prompt user for inputing 2 points
x1 = float(input('Enter x-coordinate for Point 1: '))
y1 = float(input('Enter y-coordinate for Point 1: '))
x2 = float(input('Enter x-coordinate for Point 2: '))
y2 = float(input('Enter y-coordinate for Point 2: '))

# Compute the distance between the 2 points
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display the 2 points and connect the line
turtle.penup()
turtle.goto(x1, y1)     # Go to (x1, y1)
turtle.pendown()
turtle.write('Point 1', font=('Times', 12))
turtle.goto(x2, y2)     # Draw a line to (x2, y2)
turtle.write('Point 2', font=('Times', 12))

# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance, font=('Times', 12))

turtle.done()
