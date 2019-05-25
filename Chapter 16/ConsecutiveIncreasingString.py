'''
(Maximum consecutive increasingly ordered substring)

Write a program that prompts the user to enter a string and displays the
maximum consecutive increasingly ordered substring. Analyze the time
complexity of your program. Here is a sample run:

Sample Run

Enter a string: Welcome

Maximum consecutive substring is Wel
'''


def main():
    s = input("Enter a string: ")
    print("Maximum consecutive substring is", consecutive_substring(s))
    print("Maximum consecutive substring is", consecutive_substring1(s))


def consecutive_substring(s):
    # Brute Force - Time Complexicity: O(n^2)
    substring = [s[0]]
    max_substring = s[0]

    # Loop through each letter, starting at index 1
    for index in range(1, len(s)):
        # if current letter is > previous letter, it's part of a substring
        if s[index - 1] < s[index]:
            substring.append(s[index])
        # current letter < previous letter, substring breaks
        else:
            # Compare current length of substring to the max substring
            # If current substring is bigger, we have a new max substring
            if len(substring) > len(max_substring):
                max_substring = ''.join(substring)
                substring = [s[index]]      # Reset
            else:
                # Start the substring over
                substring = [s[index]]

    return max_substring if len(max_substring) > len(substring) else ''.join(substring)


def consecutive_substring1(s):
    # Time Complexicity: O(n)
    current_substring_length = 1
    max_length = 1
    last_index_max_substring = 0

    # Loop through each letter of s, O(n)
    for i in range(1, len(s)):
        # Compare to previous letter
        # If current letter > previous letter
        if s[i] > s[i - 1]:
            current_substring_length += 1
        # current letter < previous letter, substring is broken
        else:
            # Compare current substring to max substring
            if current_substring_length > max_length:
                max_length = current_substring_length
                last_index_max_substring = i

            # Resets the length of the current string
            current_substring_length = 1

    # Check the case where max substring might be at end of s
    if current_substring_length > max_length:
        max_length = current_substring_length
        last_index_max_substring = len(s)

    return s[last_index_max_substring - max_length:last_index_max_substring]


main()
