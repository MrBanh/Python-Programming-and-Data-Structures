def main():
    text = input("Enter a text: ")
    pattern = input("Enter a string pattern: ")

    index = match(text, pattern)
    if index > 0:
        print("matched at index", index)
    else:
        print("unmatched")


def match(text, pattern):
    # len(text) - len(pattern) so we don't get IndexError
    for i in range(len(text) - len(pattern) + 1):
        if is_matched(i, text, pattern):
            return i

    # If no match for pattern
    return -1


# Test if pattern matches text starting at index i
def is_matched(i, text, pattern):
    # Go through each character in the pattern
    for k in range(len(pattern)):
        # Compare each character of pattern to a section of the text
        # If a character does not match a character in text
        if pattern[k] != text[i + k]:
            return False

    # If a pattern is discovered
    return True


main()
