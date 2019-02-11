'''
(Compute the volume of a cylinder)
Write a program that reads in the radius and length of a
cylinder and computes the area and volume
'''
import math


def cylinder_area(radius: float) -> float:
    return radius ** 2 * math.pi


def cylinder_volume(area: float, length: float) -> float:
    return area * length


if __name__ == "__main__":
    radius = float(input('Enter the radius of the cylinder: '))
    length = float(input('Enter the length of the cylinder: '))

    # Process: calculate the area and store in a variable
    area = cylinder_area(radius)    
    # Process: calculate the volume of the cylinder
    volume = cylinder_volume(area, length)

    print(f'The area of the cylinder is {area}')
    print(f'The volume of the cylinder is {volume}')
