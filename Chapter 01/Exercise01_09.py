"""
(Area and perimeter of a rectangle) 
Write a program that displays the area and perimeter 
of a rectangle with the width of 4.5 and height of 7.9 
using the following formula:

area=width×height
"""


def rectangle_area(width: float, height: float) -> None:
    area = round(width * height, 4)
    print('\narea = width x height', '\n==>', end='')
    print(area)


def rectangle_perimeter(width: float, height: float) -> None:
    perimeter = 2 * width + 2 * height
    print('\nperimeter = 2 x width + 2 x height', '\n==>', end='')
    print(perimeter)


if __name__ == "__main__":
    width = 4.5
    height = 7.9
    rectangle_area(width, height)
    rectangle_perimeter(width, height)
