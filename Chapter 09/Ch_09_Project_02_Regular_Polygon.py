'''
(Geometry: n-sided regular polygon)

An n-sided regular polygon’s sides all have the same length and all of its
angles have the same degree (i.e., the polygon is both equilateral and
equiangular). Design a class named RegularPolygon that contains:

- A private int data field named n that defines the number of sides in the
polygon.
- A private float data field named side that stores the length of the side.
- A private float data field named x that defines the x-coordinate of the
center of the polygon with default value 0.
- A private float data field named y that defines the y-coordinate of the
center of the polygon with default value 0.
- A constructor that creates a regular polygon with the specified n
(default 3), side (default 1), x (default 0), and y (default 0).
- The accessor and mutator methods for all data fields.
- The method getPerimeter() that returns the perimeter of the polygon.
- The method getArea() that returns the area of the polygon.
The formula forcomputing the area of a regular polygon is
area = (n * s^2) / (4 * tan(PI / n)).

Write a test program that creates three RegularPolygon objects, created using
RegularPolygon(), RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8).
For each object, display its perimeter and area.
'''
import math


class RegularPolygon:
    def __init__(self, n: int=3, side: float=1, x: float=0, y: float=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    # Setters (Mutators)
    def set_n(self, n: int) -> None:
        self.__n = n

    def set_side(self, side: float) -> None:
        self.__side = side

    def set_x(self, x: float) -> None:
        self.__x = x

    def set_y(self, y: float) -> None:
        self.__y = y

    # Getters (Accessors)
    def get_n(self) -> int:
        return self.__n

    def get_side(self) -> float:
        return self.__side

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def getPerimeter(self) -> float:
        return self.__n * self.__side

    def getArea(self) -> float:
        return (self.__n * self.__side ** 2) /\
               (4 * math.tan(math.pi / self.__n))


def main():
    rp = RegularPolygon()
    rp1 = RegularPolygon(6, 4)
    rp2 = RegularPolygon(10, 4, 5.6, 7.8)

    print(rp.getPerimeter(), rp.getArea())
    print(rp1.getPerimeter(), rp1.getArea())
    print(rp2.getPerimeter(), rp2.getArea())


main()
