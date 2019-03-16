'''
(Sorted?)
Write a test program that prompts the user to enter a list of numbers
separated by a space in one line and displays whether the list is
sorted or not
'''


def main():
    items = input("Enter list: ")
    nums = [int(num) for num in items.split(' ')]

    if isSorted(nums):
        print("The list is already sorted")
    else:
        print("The list is not sorted")


def isSorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False

    return True


if __name__ == "__main__":
    main()
