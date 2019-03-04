'''
(Count positive and negative numbers and compute the average of numbers)

Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the total
and average of the input values (not counting zeros). Your program ends with
the input 0. Display the average as a floating-point number.
'''

positive_nums = 0
negative_nums = 0
total = 0

while True:
    num = int(input("Enter an integer, the input ends if it is 0: "))
    if num == 0:
        break
    elif num > 0:
        positive_nums += 1
        total += num
    else:
        negative_nums += 1
        total += num
if (positive_nums + negative_nums) > 0:
    avg = total / (positive_nums + negative_nums)
    print("The number of positives is", positive_nums)
    print("The number of negatives is", negative_nums)
    print("The total is", total)
    print("The average is", avg)
else:
    print("You didn't enter any number")
