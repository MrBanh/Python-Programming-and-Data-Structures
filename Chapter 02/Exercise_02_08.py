'''
(Science: calculate energy)
Write a program that calculates the energy needed to heat water from an
initial temperature to a final temperature. Your program should prompt
the user to enter the amount of water in kilograms and the initial and
final temperatures of the water.

Formula:
Q = M * (finalTemperature – initialTemperature) * 4184

M = Weight of water in kilograms
Temperature = degrees in celsius
Q = joules
'''

amount_of_water = float(input('Enter the amount of water in kilograms: '))
initial_temp = float(input('Enter the initial temperature in Celsius: '))
final_temp = float(input('Enter the final temperature in Celsius: '))

energy_needed = amount_of_water * (final_temp - initial_temp) * 4184

print(f'The energy needed is {energy_needed}')
