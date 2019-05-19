'''
(Decimal to binary)

Write a recursive function that converts a decimal number into a binary number
as a string. The function header is as follows:

def decimalToBinary(value):

Write a test program that prompts the user to enter a decimal number and
displays its binary equivalent
'''


def main():
    n = int(input("Enter a decimal integer: "))
    print(n, "is binary", decimalToBinary(n))


def decimalToBinary(value):
    if value <= 1:
        return str(value)
    else:
        return decimalToBinary(value // 2) + str(value % 2)


main()
