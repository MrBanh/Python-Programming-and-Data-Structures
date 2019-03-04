'''
(Count vowels and consonants)

Assume letters A, E, I, O, and U as the vowels.
Write a program that prompts the user to enter a
string and displays the number of vowels and consonants
in the string.
'''

vowels = "AEIOUaeiou"
num_of_consonants = 0
num_of_vowels = 0

str_input = input("Enter a string: ")
for ch in str_input:
    if ch in vowels:
        num_of_vowels += 1
    elif ch.isalpha():
        num_of_consonants += 1

print("The number of vowels is", num_of_vowels)
print("The number of consonants is", num_of_consonants)
