'''
(Geometry: area of a hexagon)
Write a program that prompts the user to enter the side of a hexagon and
displays its area.

Formula:

Area= (3 * (3 ** 0.5)) / 2 * s ** 2

s = length of side

'''

side = float(input('Enter the side length of the hexagon: '))
area = (3 * (3 ** 0.5)) / 2 * side ** 2

print(f'The area of the hexagon is {area}')
