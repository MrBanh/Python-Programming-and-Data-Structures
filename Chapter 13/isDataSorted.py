'''
(Data sorted?)

Write a program that prompts the user to read a filename and reads the words
from the file and reports whether the words in the files are stored in
ascending order. If the words are not sorted in the file, display the first
two words that are out of the order.
'''


def main():
    try:
        filename = input("Enter a filename: ").strip()
    except IOError:
        pass

    with open(filename, 'r') as file:
        str_list = file.read().split()

    current_word = str_list[0]

    is_sorted = True
    for i in range(1, len(str_list)):
        next_word = str_list[i]
        if next_word[0] < current_word[0]:
            is_sorted = False
            break
        else:
            current_word = next_word

    if is_sorted:
        print("The words are sorted.")
    else:
        print("The words are not sorted. The first two out-of-order words:", current_word, next_word)


main()
