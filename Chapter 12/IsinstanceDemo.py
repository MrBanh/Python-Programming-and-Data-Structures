from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle


def main():
    c = Circle(4)
    r = Rectangle(1, 3)
    print("Circle...")
    displayObject(c)
    print("Rectangle...")
    displayObject(r)


def displayObject(g):
    print("Area is", g.get_area())
    print("Perimeter is", g.get_perimeter())

    if isinstance(g, Circle):
        print("Diameter is", g.get_diameter())
    elif isinstance(g, Rectangle):
        print("Width is", g.get_width())
        print("Height is", g.get_height())


main()
