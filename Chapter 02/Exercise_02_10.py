'''
(Physics: find runway length)
Given an airplane’s acceleration a and take-off speed v,
you can compute the minimum runway length needed for an airplane
to take off using the following formula:

length = (v ** 2) / (2 * a)

Write a program that prompts the user to enter v in meters/second (m/s),
the acceleration a in meters/second squared (m/s2), and then displays the
minimum runway length.
'''


velocity = float(input('Enter speed: '))
acceleration = float(input('Enter acceleration: '))

length = (velocity ** 2 ) / (2 * acceleration)

print(f'The minimum runway length for this airplane is {length} meters')
