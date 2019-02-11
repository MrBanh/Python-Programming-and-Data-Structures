'''
(Financial application: calculate tips)
Write a program that reads the subtotal and the gratuity rate and
computes the gratuity and total. For example, if the user enters 10
for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.
'''


subtotal = float(input('Enter the subtotal: '))
subtotal = int(subtotal * 100) / 100

gratuity_rate = float(input('Enter the gratuity rate: '))
gratuity_rate /= 100        # Convert to decimal
gratuity = int((subtotal * gratuity_rate) * 100) / 100

total = round(subtotal + gratuity, 2)

print(f'The gratuity is {gratuity} and the total is {total}')
