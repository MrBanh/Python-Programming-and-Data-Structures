'''
(Count consonants and vowels)

Write a program that prompts the user to enter a text in one line and displays
the number of vowels and consonants in the text. Use a set to store the vowels
A, E, I, O, and U.
'''


def main():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    text = input("Enter a text: ").strip().lower()
    text_list = list(text.replace(" ", ''))
    count_vowels = 0

    for ch in text_list:
        if ch in vowels:
            count_vowels += 1

    print("The number of vowel is", count_vowels, "and consonants is", len(text_list) - count_vowels)


main()
