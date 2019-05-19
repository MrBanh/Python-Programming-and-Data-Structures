def is_palindrome(s: list) -> bool:
    return is_palindrome_helper(s, 0, len(s) - 1)


def is_palindrome_helper(s: list, low: int, high: int) -> bool:
    # exhausted list
    if high <= low:
        return True
    elif s[low] != s[high]:
        return False
    else:
        return is_palindrome_helper(s, low + 1, high - 1)


def main():
    print("Is moon a palindrome?", is_palindrome("moon"))
    print("Is noon a palindrome?", is_palindrome("noon"))
    print("Is a a palindrome?", is_palindrome("a"))
    print("Is aba a palindrome?", is_palindrome("aba"))
    print("Is ab a palindrome?", is_palindrome("ab"))


if __name__ == "__main__":
    main()
