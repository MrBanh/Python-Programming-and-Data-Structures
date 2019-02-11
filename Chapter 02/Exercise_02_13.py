'''
(Split digits)
Write a program that prompts the user to enter a four-digit
integer and displays the number in reverse order.
'''

num_str = input('Enter an integer: ')

for i in range(len(num_str) - 1, -1, -1):
    print(num_str[i])
