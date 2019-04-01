'''
(Split a string)
Write the following function that splits a string into substrings using
delimiter characters.

def split(s, delimiters);

For example, split("AB#C D?EF#45", "# ?") returns a list containing
AB, C, D, EF, and 45. Write a test program that prompts the user to enter
a string and delimiters and displays the substrings separated by exactly
one space.

(You are not allowed to use the regex for splitting a string in this exercise.)

SAMPLE RUN:

Enter a string: Welcome to Python

Enter delimiters: oe
W lc m t Pyth n
'''


def main():
    s = input("Enter a string: ")
    delimiters = input("Enter delimiters: ")
    print(' '.join(split(s, delimiters)))


def split(s, delimiters):
    substring = []

    temp_s = ''
    for ch in s:
        if ch not in delimiters:
            temp_s += ch
        else:
            substring.append(temp_s)
            temp_s = ''

    if temp_s:
        substring.append(temp_s)

    return substring

main()
