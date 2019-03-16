'''
(Count occurrence of numbers)

Write a program that reads some integers between 1 and 100
and counts the occurrences of each. Note that if a number
occurs more than one time, the plural word “times” is used
in the output. Note the integers are entered in one line
separated by a space.
'''

int_input = input("Enter integers between 1 and 100, inclusive: ")
int_list = [int(num) for num in int_input.split(' ')]
unique_integers = []

for num in int_list:
    if num not in unique_integers:
        unique_integers.append(num)

unique_integers.sort()

for num in unique_integers:
    occurrences = int_list.count(num)
    if occurrences > 1:
        print(str(num), "occurs", str(occurrences), "times")
    else:
        print(str(num), "occurs", str(occurrences), "time")
