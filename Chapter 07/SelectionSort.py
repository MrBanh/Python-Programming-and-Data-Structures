'''SelectionSort.py

Example of Selection Sort
In Ascending Order: takes the smallest number, swaps it with first element
                    takes next smallest number, swaps with 2nd element
                    and so on
In Descending Order: takes the biggest number...

Space and Time Comoplexity: O(n^2)

'''


def main():
    lst = [-2, 4.5, 5, 1, 90, 2, -3.3, 90]
    selection_sort(lst)
    print(lst)
    selection_sort(lst, Ascending=False)
    print(lst)


def selection_sort(lst, Ascending: bool = True):
    if Ascending:
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[i]:
                    lst[i], lst[j] = lst[j], lst[i]
    else:
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                if lst[j] > lst[i]:
                    lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    main()
