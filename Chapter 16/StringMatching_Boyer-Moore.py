def main():
    text = input("Enter a text: ")
    pattern = input("Enter a string pattern: ")

    index = match(text, pattern)
    if index >= 0:
        print("matched at index", index)
    else:
        print("unmatched")


def match(text, pattern):
    i = len(pattern) - 1        # Since lists start at index 0
    while i < len(text):
        k = i
        j = len(pattern) - 1
        while j >= 0:
            # Look at the first section of text that is len(pattern) - 1
            # Compare the last letter of that section to last letter of pattern
            if text[k] == pattern[j]:
                # Character matches, go to the letter prior to compare
                k -= 1
                j -= 1
            else:
                break

        # If the section is exhausted when comparing letter backwards
        # without breaking loop, the pattern matches
        if j < 0:
            return i - len(pattern) + 1

        # If the inner while loop breaks, there was a mismatch
        # Find the last index and character of pattern that matches text[k]
        u = find_last_index(text[k], j - 1, pattern)

        # if there is a character in pattern that matches text[k]
        # include text[k] the pattern character in the next section
        # comparison to pattern
        if u >= 0:
            i = k + len(pattern) - 1 - u
        # pattern does not include text[k],
        # move past the character at text[k]
        else:
            i = k + len(pattern)

    # No pattern match
    return -1


# Return the index of the last element in pattern[0 .. j]
# that matches ch. -1 otherwise.
def find_last_index(ch, j, pattern):
    # Loop through the remaining characters in pattern that was not compared
    for k in range(j, -1, -1):
        # If the character from text[k] matches 1 of the remaining characters
        # in pattern
        if ch == pattern[k]:
            # return the index of the pattern where the letters matches text[k]
            return k

    return -1
