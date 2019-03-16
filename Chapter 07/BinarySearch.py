'''BinarySearch.py

Example of a Binary Search. The idea is with each search,
divide the number of items to search by 1 with each iteration

The algorithm is: n / (2 ** k) = 1
Given an n-length list, it will take k-number of iterations, 
assuming we end up searching through the whole list.

-> n = 2 ** k
-> log2(n) = k

Time and Space Complexity: O(log2n)
'''


def main():
    lst = [-3, 1, 2, 4, 9, 23]
    print(binary_search(lst, 50))


# Returns the index of found element, if not found return -1
def binary_search(lst, key) -> int:
    low = 0     # starting low index is 0
    high = len(lst) - 1     # starting high index

    while high >= low:
        mid = (high + low) // 2     # mid index

        # key is less than the value at middle index
        if key < lst[mid]:
            # new high index is the index before mid
            high = mid - 1

        # key is greater than the value at middle index
        elif key > lst[mid]:
            # new low index is the index after mid
            low = mid + 1

        # key is at the middle index
        else:
            return mid

    return -low - 1     # Key not found


if __name__ == "__main__":
    main()
