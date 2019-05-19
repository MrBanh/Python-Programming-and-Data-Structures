def sort(lst: list) -> None:
    sort_helper(lst, 0, len(lst) - 1)


def sort_helper(lst: list, low: int, high: int) -> None:
    if low < high:
        # Find the smallest number and its index
        index_of_smallest = low
        smallest_num = lst[low]

        for i in range(low + 1, high + 1):
            if lst[i] < smallest_num:
                index_of_smallest = i
                smallest_num = lst[i]

        # Swap values, putting the smallest at lst[low]
        lst[index_of_smallest] = lst[low]
        lst[low] = smallest_num

        # Sort the remaining lst[low + 1... high]
        sort_helper(lst, low + 1, high)


def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
