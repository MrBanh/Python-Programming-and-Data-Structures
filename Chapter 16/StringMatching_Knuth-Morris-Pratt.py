def main():
    text = input("Enter a text: ")
    pattern = input("Enter a string pattern: ")

    index = match(text, pattern)
    if index >= 0:
        print("matched at index", index)
    else:
        print("unmatched")


def match(text, pattern):
    f = get_failure(pattern)
    i = 0       # Index on text
    k = 0       # Index on pattern

    while i < len(text):
        if text[i] == pattern[k]:
            if k == len(pattern) - 1:
                return i - len(pattern) + 1     # Matched
            i += 1
            k += 1
        else:
            if k > 0:
                k = f[k -1]     # Match prefix position
            else:
                i += 1      # No prefix

    return -1


def get_failure(pattern):
    fail = len(pattern) * [0]
    k = 0       # Starting at pattern[0]
    i = 1       # Starting at pattern[1]

    # Loop through all characters of pattern
    while i < len(pattern):
        # If a character at pattern[i] == character at pattern[k]
        if pattern[i] == pattern[k]:
            fail[i] = k + 1     # fail[i] = Index k + 1
            # Move to pattern[i + 1] and pattern[k + 1]
            i += 1
            k += 1
        elif k > 0:
            # Set k to the index of the value stored in fail[k-1]
            k = fail[k - 1]
        else:
            # Move to pattern[i + 1] if the characters don't match
            i += 1

    # Return the list
    return fail


main()
