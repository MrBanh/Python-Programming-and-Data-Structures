'''
(Display nonduplicate words in ascending order)

Write a program that prompts the user to enter a text in one line and displays
all the nonduplicate words in ascending order.
'''


def main():
    text = input("Enter a text: ").strip()
    text_set = set(text.split())
    non_dup_list = list(sorted(text_set))
    for word in non_dup_list:
        print(word, end=' ')


main()
