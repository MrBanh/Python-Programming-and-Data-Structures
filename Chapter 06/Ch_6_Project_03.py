'''
(Occurrences of a specified character)

Write a function that finds the number of occurrences of a specified character
in the string using the following header:

def count(s, ch):

For example, count("Welcome", 'e') returns 2. The str class has the count
method. Implement your method without using the count method. Write a test
program that reads a string and a character and displays the number of
occurrences of the character in the string.
'''


def count(s, ch):
    count = 0
    for char in s:
        if char == ch:
            count += 1

    return count


def main():
    str_input = input("Enter a string: ")
    char_input = input("Enter a character: ")
    print(char_input, "appears in", str_input, str(count(str_input, char_input)), "times")


main()