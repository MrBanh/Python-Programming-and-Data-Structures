'''
(Health application: compute BMI)
Body mass index (BMI) is a measure of health based on weight.
It can be calculated by taking your weight in kilograms and dividing
it by the square of your height in meters. Write a program that
prompts the user to enter a weight in pounds and height in inches
and displays the BMI. Note that one pound is 0.45359237 kilograms
and one inch is 0.0254 meters.
'''


weight_pounds = float(input('Enter weight in pounds: '))
weight_kilograms = weight_pounds * .45359237
height_inches = float(input('Enter height in inches: '))
height_meters = height_inches * .0254

bmi = weight_kilograms / (height_meters ** 2)

print(f'BMI is {bmi}')
