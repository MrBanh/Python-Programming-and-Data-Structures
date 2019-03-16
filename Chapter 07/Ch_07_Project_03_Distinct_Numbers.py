'''
(Print distinct numbers)

Write a program that reads in integers separated by a space in one line
and displays distinct numbers in their input order and separated by
exactly one space (i.e., if a number appears multiple times, it is
displayed only once).

Hint: Read all the numbers and store them in list1. Create a new list list2.
Add a number in list1 to list2. If the number is already in the list, ignore
it.
'''

items = input("Enter numbers: ")
nums = [int(num) for num in items.split(' ')]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print("The distinct numbers are:", ' '.join(str(num) for num in unique_nums))
