'''
(Geometry: point in a rectangle?)

Write a program that prompts the user to enter a point (x, y) and
checks whether the point is within the rectangle centered at (0, 0) with width 10 and height 5.

For example, (2, 2) is inside the rectangle and (6, 4) is outside the rectangle
'''

x_coord = float(input('Enter the x-coordinate of the point: '))
y_coord = float(input('Enter the y-coordinate of the point: '))

RECTANGLE_WIDTH = 10
RECTANGLE_HEIGHT = 5

if abs(x_coord) > (RECTANGLE_WIDTH / 2) or abs(y_coord) > (RECTANGLE_HEIGHT / 2):
    print('Point (' + str(x_coord) + ', ' + str(y_coord) + ') is not in the rectangle')
else:
    print('Point (' + str(x_coord) + ', ' + str(y_coord) + ') is in the rectangle')
