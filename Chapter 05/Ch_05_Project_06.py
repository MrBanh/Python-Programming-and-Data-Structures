'''
(Business: check ISBN-13)

ISBN-13 is a new standard for indentifying books.
It uses 13 digits d1d2d3d4d5d6d7d8d910d11d12d13 .
The last digit d13 is a checksum, which is calculated
from the other digits using the following formula:

10-(d1+ 3*d2 + d3+ 3*d4 + d5 + 3*d6 + d7 + 3*d8 + d9 + 3*d10 + d11 + 3*d12)%10

If the checksum is 10, replace it with 0.
Your program should read the input as a string.
Display “incorrect input” if the input is incorrect.
'''
import sys

isbn_13 = input("Enter the first 12 digits of an ISBN-13 as a string: ")
sums = 0        # Keeps track of the d1 + 3*d2 + d3 + .. + 3*d12
checksum = 0

if len(isbn_13) != 12:
    print("Incorrect input")
    sys.exit()

# Go through each character of user input
for i in range(len(isbn_13)):
    if (i + 1) % 2 == 0:
        sums += (3 * int(isbn_13[i]))
    else:
        sums += int(isbn_13[i])

# Calculate checksum
checksum = 10 - sums % 10

# If checksum is 10, replace with 0
if checksum == 10:
    checksum = 0

# Display ISBN-13 number
print("The ISBN-13 number is", isbn_13 + str(checksum))
