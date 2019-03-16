'''
(Anagrams)

Write a function that checks whether two words are anagrams.
Two words are anagrams if they contain the same letters.
For example, silent and listen are anagrams.

The header of the function is:

    def isAnagram(s1, s2):

(Hint: Obtain two lists for the two strings.
Sort the lists and check if two lists are identical.)

Write a test program that prompts the user to enter two strings
and checks whether they are anagrams.
'''


def main():
    s1 = input("Enter a string s1: ")
    s2 = input("Enter a string s2: ")

    if isAnagram(s1, s2):
        print(s1, "and", s2, "are anagrams")
    else:
        print(s1, "and", s2, "are not anagrams")


def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    ch1 = list(s1)
    ch2 = list(s2)

    ch1.sort()
    ch2.sort()

    return ch1 == ch2


if __name__ == "__main__":
    main()
