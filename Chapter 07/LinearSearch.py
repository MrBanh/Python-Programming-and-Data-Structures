'''LinearSearch.py

Example of a linear search

Space and time complexity: O(n)
'''


def main():
    # Test case
    lst = [4, 5, 1, 2, 9, -3]
    print(linear_search(lst, 2))


# Returns index of first occurance of key
def linear_search(lst, key) -> int:
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    
    return -1       # Not found


if __name__ == "__main__":
    main()
