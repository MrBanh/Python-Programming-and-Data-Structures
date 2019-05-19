def binary_search(lst: list, key: int) -> int:
    return binary_search_helper(lst, key, 0, len(lst) - 1)


def binary_search_helper(lst: list, key: int, low: int, high: int) -> int:
    if low > high:
        return -1

    mid = (low + high) // 2
    if key < lst[mid]:
        return binary_search_helper(lst, key, low, mid - 1)
    elif key == lst[mid]:
        return mid
    else:
        return binary_search_helper(lst, key, mid + 1, high)


def main():
    lst = [3, 5, 6, 8, 9, 12, 34, 36]
    print(binary_search(lst, 3))
    print(binary_search(lst, 4))


if __name__ == "__main__":
    main()
