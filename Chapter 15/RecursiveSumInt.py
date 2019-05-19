'''
(Sum the digits in an integer using recursion)

Write a recursive function that computes the sum of the digits in an integer.
Use the following function header:

def sumDigits(n):

For example, sumDigits(234) returns 9.

Write a test program that prompts the user to enter an integer and displays
the sum of its digits.
'''


def main():
    n = int(input("Enter an integer: "))
    # Display result
    print("The sum of digits in", n, "is", sumDigits(n))


def sumDigits(n):
    # Using recursive helper function
    # return sumDigits_helper(str(n), 0, 0)

    # Just using recursion
    if n == 0:
        return n
    else:
        return sumDigits(n // 10) + n % 10


# def sumDigits_helper(n, index, result):
#     if index == (len(n) - 1):
#         return result + int(n[index])
#     else:
#         return sumDigits_helper(n, index + 1, result + int(n[index]))


main()
