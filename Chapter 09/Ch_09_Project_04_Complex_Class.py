'''
(Math: The Complex class)
Python has the complex class for performing complex number arithmetic.
In this exercise, you will design and implement your own Complex class.

Note that the complex class in Python is named in lowercase,
but our custom Complex class is named with C in uppercase.

A complex number is a number of the form a+bi, where a and b are real numbers
and i is sq root of -1.

The numbers a and b are known as the real part and the imaginary part of the
complex number, respectively.

You can perform addition, subtraction, multiplication, and division for complex
numbers using the following formulas:

(a + bi) + (c + di) = (a + c) + (b + d)i
(a + bi) − (c + di) = (a − c) + (b − d)i
(a + bi) * (c + di) = (ac − bd) + (bc + ad)i
(a + bi) / (c + di) = (ac + bd) / (c2 + d2) + (bc − ad)i / (c2 + d2)

You can also obtain the absolute value for a complex number using the
following formula:

abs(a + bi) = ((a ** 2) + (b ** 2)) ** 0.5


The absolute value of the complex number corresponds to the distance of the
point to the origin

Point (2, 3) can be written as a complex number (2 + 3i) and
(3, −2) as (3 − 2i).

Design a class named Complex for representing complex numbers and the
methods __add__, __sub__, __mul__, __truediv__, and __abs__ for performing
complex-number operations, and override the __str__ method by returning a
string representation for a complex number. The __str__ method returns (a + bi)
as a string. If b is 0, it simply returns a.

Provide a constructor Complex(a, b) to create a complex number a+bi with the
default value of 0 for a and b. Also provide the getReal() and
getImaginary() methods for returning the real and imaginary parts of the
complex number, respectively.

Write a test program that prompts the user to enter two complex numbers and
displays the result of their addition, subtraction, multiplication, division,
and absolute value.

EXAMPLE:

Enter the real part of the first complex number: 3.5
Enter the imaginary part of the first complex number: 6.5
Enter the real part of the second complex number: -3.5
Enter the imaginary part of the second complex number: 1
(3.5 + 6.5i) + (-3.5 + 1.0i) = (0.0 + 7.5i)
(3.5 + 6.5i) - (-3.5 + 1.0i) = (7.0 + 5.5i)
(3.5 + 6.5i) * (-3.5 + 1.0i) = (-18.75 + -19.25i)
(3.5 + 6.5i) / (-3.5 + 1.0i) = (-0.4339622641509434 + -1.9811320754716981i)
|(3.5 + 6.5i)| = 4.47213595499958
'''


class Complex:
    def __init__(self, real_part=0, imaginary_part=0):
        self.__real_part = real_part
        self.__imaginary_part = imaginary_part

    def getReal(self):
        return self.__real_part

    def getImaginary(self):
        return self.__imaginary_part

    # (a + bi) + (c + di) = (a + c) + (b + d)i
    def __add__(self, other):
        # (a + c)
        real_part = self.getReal() + other.getReal()

        # (b + d)
        imaginary_part = self.getImaginary() + other.getImaginary()

        return Complex(real_part, imaginary_part)

    # (a + bi) − (c + di) = (a − c) + (b − d)i
    def __sub__(self, other):
        # (a − c)
        real_part = self.getReal() - other.getReal()

        # (b − d)
        imaginary_part = self.getImaginary() - other.getImaginary()

        return Complex(real_part, imaginary_part)

    # (a + bi) * (c + di) = (ac − bd) + (bc + ad)i
    def __mul__(self, other):
        # ac - bd
        real_part = (self.getReal() * other.getReal()) -\
                    (self.getImaginary() * other.getImaginary())

        # bc + ad
        imaginary_part = (self.getImaginary() * other.getReal()) +\
                         (self.getReal() * other.getImaginary())

        return Complex(real_part, imaginary_part)

    # (a + bi) / (c + di) = (ac + bd)/(c**2 + d**2) + (bc − ad)i/(c**2 + d**2)
    def __truediv__(self, other):
        # (ac + bd) / (c**2 + d**2)
        real_part = ((self.getReal() * other.getReal()) +
                     (self.getImaginary() * other.getImaginary())) /\
                    (other.getReal() ** 2 + other.getImaginary() ** 2)

        # (bc − ad)/(c**2 + d**2)
        imaginary_part = ((self.getImaginary() * other.getReal()) -
                          (self.getReal() * other.getImaginary())) /\
                         (other.getReal() ** 2 + other.getImaginary() ** 2)

        return Complex(real_part, imaginary_part)

    # abs(a + bi) = ((a ** 2) + (b ** 2)) ** 0.5
    def __abs__(self):
        return Complex((self.getReal() ** 2 + self.getImaginary() ** 2) ** 0.5)

    # returns (a + bi) or just "a" if imaginary part is 0
    def __str__(self):
        if self.__imaginary_part == 0:
            return str(self.__real_part)
        else:
            return "(" + str(self.__real_part) + " + " +\
                   str(self.__imaginary_part) + "i)"


def main():
    a = float(input("Enter the real part of the first complex number: "))
    b = float(input("Enter the imaginary part of the first complex number: "))
    c = float(input("Enter the real part of the second complex number: "))
    d = float(input("Enter the imaginary part of the second complex number: "))

    comp_num1 = Complex(a, b)
    comp_num2 = Complex(c, d)

    # Display results
    print(comp_num1, '+', comp_num2, '=', comp_num1 + comp_num2)
    print(comp_num1, '-', comp_num2, '=', comp_num1 - comp_num2)
    print(comp_num1, '*', comp_num2, '=', comp_num1 * comp_num2)
    print(comp_num1, '/', comp_num2, '=', comp_num1 / comp_num2)
    print('|' + str(comp_num1) + '|', '=', abs(comp_num1))
    print('|' + str(comp_num2) + '|', '=', abs(comp_num2))

main()
