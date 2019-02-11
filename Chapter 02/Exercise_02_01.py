'''
(Convert Celsius to Fahrenheit)
Write a program that reads a Celsius degree from the console
and converts it to Fahrenheit and displays the result.
'''


def celsius_to_fahrenheight(celsius: float) -> float:
    return (9 / 5) * celsius + 32


if __name__ == "__main__":
    celsius = float(input('Enter the temperature in celsius: '))
    print(f'{celsius} Celsius is {celsius_to_fahrenheight(celsius)} Fahrenheight')
