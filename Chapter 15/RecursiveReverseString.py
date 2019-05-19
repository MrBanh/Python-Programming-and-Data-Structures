'''
(Print the characters in a string reversely)

Write a recursive function that displays a string reversely on the console
using the following header:

def reverseDisplay(value):

For example, reverseDisplay("abcd") displays dcba. Write a test program that
prompts the user to enter a string and displays its reversal.
'''


def main():
    s = input("Enter a string: ")
    reverseDisplay(s)


def reverseDisplay(value):
    reverseDisplay_helper(value, len(value) - 1)


def reverseDisplay_helper(value, index):
    if index != -1:
        print(value[index], end='')
        reverseDisplay_helper(value, index - 1)

main()
