'''
(Count the occurrences of each keyword)

Write a program that reads in a Python source code as a one-line text and
counts the occurrence of each keyword in the file. Display the keyword
and count in ascending order on keywords.
'''
import keyword


def main():
    src_code = input("Enter Python source code: ").strip().split()
    keywords = {}

    # Go through the src code
    for word in src_code:
        if word in keyword.kwlist:
            # If we're already tracking the word in a dictionary
            if word in keywords:
                keywords[word] += 1
            # If not, start tracking
            else:
                keywords[word] = 1

    # Convert dictionary into list to sort
    keyswords_list = list(keywords.items())
    keyswords_list.sort()

    # Display results
    for kword, count in keyswords_list:
        print(kword + ":", count)


main()
