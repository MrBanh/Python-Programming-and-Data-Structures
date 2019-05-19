'''
(Binary to decimal)

Write a recursive function that parses a binary number as a string into a
decimal integer. The function header is as follows:

def binaryToDecimal(binaryString):

Write a test program that prompts the user to enter a binary string and
displays its decimal equivalent.
'''


def main():
    n = input("Enter a binary number: ")
    print(n, "is decimal", binaryToDecimal(n))


# https://www.wikihow.com/Convert-from-Binary-to-Decimal
def binaryToDecimal(binaryString):
    # Base case, if there was only 1 binary number provided
    if len(binaryString) == 1:
        return int(binaryString[0]) * (2 ** (len(binaryString) - 1))
    else:
        return int(binaryString[0]) * (2 ** (len(binaryString) - 1)) +\
            binaryToDecimal(binaryString[1:])


main()
