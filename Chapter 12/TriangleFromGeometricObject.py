from GeometricObject import GeometricObject


class Triangle(GeometricObject):
    def __init__(self, color, filled, side1=1.0, side2=1.0, side3=1.0):
        super().__init__(color=color, filled=filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    # https://www.mathopenref.com/heronsformula.html
    def getArea(self):
        p = self.getPerimeter() / 2     # Half perimeter
        return (p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3)) ** 0.5

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)


def main():
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))
    color = input("Enter color: ")
    filled = int(input("Enter 1/0 for filled (1: true, 0: false): "))

    triangle = Triangle(color, bool(filled), side1, side2, side3)

    print("The area is", triangle.getArea())
    print("The perimeter is", triangle.getPerimeter())
    print("Color is", color)
    print("Filled is", bool(filled))


main()
