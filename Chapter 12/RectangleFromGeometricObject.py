from GeometricObject import GeometricObject


class Rectangle(GeometricObject):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"{super().__str__()} width: {self.__width} height: {self.__height}"
