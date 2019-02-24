'''
(Hex to binary)

Write a program that prompts the user to enter a hex digit and displays its corresponding binary number.
'''
import sys

hex_digit = input("Enter a hex digit: ")

try:
    hex_digit_to_decimal = int(hex_digit, 16)       # Convert hex to decimal
    binary = bin(hex_digit_to_decimal)[2:]      # Convert decimal to binary using bin()
    print("The binary value is", binary)

except Exception:
    print("Invalid input")
    sys.exit()
