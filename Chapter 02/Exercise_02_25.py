'''
(Sum the digits in an integer)
Write a program that reads an integer between 0 and 1000 and
adds all the digits in the integer. For example, if an integer is 932,
the sum of all its digits is 14
'''

num = input('Enter an integer between 0 and 1000: ')
sum_of_digits = 0

for i in range(len(num)):
    sum_of_digits += int(num[i])

print(f'The sum of all digits in {num} is {sum_of_digits}')
