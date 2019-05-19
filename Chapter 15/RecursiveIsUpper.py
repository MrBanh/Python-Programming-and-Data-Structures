'''
(Find the number of uppercase letters in a string)

Write a recursive function to return the number of uppercase letters in a
string using the following function headers:

def countUppercase(s):

def countUppercaseHelper(s, high):

Write a test program that prompts the user to enter a string and displays the
number of uppercase letters in the string.
'''


def main():
    s = input("Enter a string: ")
    print("The uppercase letters in", s, "is", countUppercase(s))


def countUppercase(s):
    return countUppercaseHelper(s, 0)


def countUppercaseHelper(s, index):
    if index == len(s):
        return 0        # Reached end of string
    else:
        return (1 if s[index].isupper() else 0) +\
                countUppercaseHelper(s, index + 1)


main()
