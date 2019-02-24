'''
(Business: check ISBN-10)

An ISBN-10 (International Standard Book Number) consists of 10 digits: d1d2d3d4d5d6d7d8d9d10.
The last digit, d10, is a checksum, which is calculated from the other nine digits using the following formula:

(d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11

If the checksum is 10, the last digit is denoted as X according to the ISBN-10 convention.
Write a program that prompts the user to enter the first 9 digits and displays the 10-digit ISBN (including leading zeros).
'''
import sys

isbn_str = input('Enter the first 9 digits of an ISBN as a string: ')

if len(isbn_str) != 9:
    print('Incorrect input. It must have exact 9 digits')
    sys.exit()
else:
    total = 0
    for each_index in range(9):
        total += (int(isbn_str[each_index]) * (each_index + 1))

    checksum = total % 11

print("The ISBN-10 number is", isbn_str, end='')
if checksum == 10:
    print('X')
else:
    print(checksum)
