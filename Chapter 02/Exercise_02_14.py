'''
(Geometry: area of a triangle)
Write a program that prompts the user to enter the three points
(x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.

Formula:
side = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

'''

x_coord1 = float(input('Enter x-coordinate of Point 1 for a triangle: '))
y_coord1 = float(input('Enter y-coordinate of Point 1 for a triangle: '))
x_coord2 = float(input('Enter x-coordinate of Point 2 for a triangle: '))
y_coord2 = float(input('Enter y-coordinate of Point 2 for a triangle: '))
x_coord3 = float(input('Enter x-coordinate of Point 3 for a triangle: '))
y_coord3 = float(input('Enter y-coordinate of Point 3 for a triangle: '))

side1 = ((x_coord1 - x_coord2) ** 2 + (y_coord1 - y_coord2) ** 2) ** .5
side2 = ((x_coord2 - x_coord3) ** 2 + (y_coord2 - y_coord3) ** 2) ** .5
side3 = ((x_coord3 - x_coord1) ** 2 + (y_coord3 - y_coord1) ** 2) ** .5

s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print(f'The area of the triangle is {area}')
