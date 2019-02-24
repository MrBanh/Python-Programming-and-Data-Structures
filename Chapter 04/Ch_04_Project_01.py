'''
(Geometry: area of a regular polygon)

A regular polygon is an n-sided polygon in which all sides are of the same
length and all angles have the same degree(i.e., the polygon is both
equilateral and equiangular). The formula for computing the area of a regular
polygon is

area = (n * s^2) / (4 * tan(PI / n)

Here, s is the length of a side. Write a program that prompts the user to
enter the number of sides and their length of a regular polygon and
displays its area.
'''
import math

# Prompt user for number of sides
num_of_sides = int(input("Enter the number of sides: "))

# Prompt for length of each side
side_length = float(input("Enter the side: "))

# Compute the area of the polygon
area = (num_of_sides * (side_length ** 2)) / \
       (4 * math.tan(math.pi / num_of_sides))

# Display the result
print("The area of the polygon is", area)
