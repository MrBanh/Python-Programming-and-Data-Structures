'''
(Count vowels and consonants)

Write a program that prompts the user to enter a string and displays the
number of vowels and consonants in the string. The same vowels or consonants
are counted only once. The letters are case-insensitive. The letters for
vowels are A, E, I, O, and U. Implement it in O(1) time.

Hint: Use a set to store vowels. It takes O(1) time to test if an element is
in a set.

Sample Run

Enter a string: Programming is fun

The number of vowels is 4

The number of consonants is 7
'''


# Time Complexicity: O(1)
def main():
    s = input("Enter a string: ")       # s is the data

    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

    s_vowels = set()
    s_consonants = set()
    vowels_count = 0
    consonants_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                if char not in s_vowels:
                    s_vowels.add(char)
                    vowels_count += 1
            else:
                if char not in s_consonants:
                    s_consonants.add(char)
                    consonants_count += 1

    print("The number of vowels is", vowels_count)
    print("The number of consonants is", consonants_count)


main()
