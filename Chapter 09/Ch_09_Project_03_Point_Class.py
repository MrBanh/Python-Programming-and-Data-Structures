'''
(The Point class)
Design a class named Point to represent a point with x- and y-coordinates.

The class contains:

- Two private data fields x and y that represent the coordinates with get
methods.
- A constructor that constructs a point with specified coordinates, with
default point (0, 0).
- A method named distance that returns the distance from this point to another
point of the Point type.
- A method named isNearBy(p1) that returns true if point p1 is close to this
point. Two points are close if their distance is less than 5.
- Implement the __str__ method to return a string in the form (x, y).

Write a test program that prompts the user to enter two points, displays
the distance between them, and indicates whether they are near each other.
'''


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance(self, other):
        return ((other.get_x() - self.get_x()) ** 2 +
                (other.get_y() - self.get_y()) ** 2) ** 0.5

    def isNearBy(self, other):
        return True if self.distance(other) < 5 else False

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"


def main():
    x1 = float(input("Enter the x-coordinate of point1: "))
    y1 = float(input("Enter the y-coordinate of point1: "))
    x2 = float(input("Enter the x-coordinate of point2: "))
    y2 = float(input("Enter the y-coordinate of point2: "))

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)

    dist = point1.distance(point2)

    print("The distance between the two points is", format(dist, ".2f"))

    if point1.isNearBy(point2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")

main()
