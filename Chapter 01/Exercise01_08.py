"""
(Area and perimeter of a circle) 
Write a program that displays the area and perimeter 
of a circle that has a radius of 5.5 
using the following formula

area=radius×radius×π
perimeter=2×radius×π
"""
import math


def circle_area(r: float) -> None:
    area = r * r * math.pi
    print(f'\narea = radius x radius x π', '\n==> ', end='')
    print(area)


def circle_perimeter(r: float) -> None:
    perimeter = 2 * r * math.pi
    print(f'\nperimeter = 2 x radius x π', '\n==>', end='')
    print(perimeter)


if __name__ == "__main__":
    try:
        r = 5.5
        if r <= 0:
            raise Exception
        circle_area(r)
        circle_perimeter(r)
    except:
        print('Radius cannot be a zero or negative')
