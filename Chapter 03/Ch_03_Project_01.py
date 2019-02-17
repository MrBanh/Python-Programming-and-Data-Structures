'''
(Algebra: solve quadratic equations)

The two roots of a quadratic equation, for example, , can be obtained using the following formula:

r1 = (-b + sqrt(b^2 - 4ac) / (2a) and r1 = (-b - sqrt(b^2 - 4ac) / (2a)

b^2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots. If it is zero, the equation has one root.
If it is negative, the equation has no real roots.

Write a program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant.

If the discriminant is positive, display two roots.

If the discriminant is 0, display one root.

Otherwise, display “The equation has no real roots”.
'''
import math


# Prompt user for a, b, and c
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# Calculate the discrimnant, which is b^2 - 4ac
discriminant = b ** 2 - 4 * a * c

# If discrimnant is positive, there are 2 roots
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print('The roots are', root1, 'and', root2)

elif discriminant == 0:
    root = (-b - math.sqrt(discriminant)) / (2 * a)
    print('The root is', root)

else:
    print('The equation has no real roots')
