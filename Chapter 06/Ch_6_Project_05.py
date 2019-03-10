'''
(Binary to hex)

Write a function that parses a binary number into a hex number.

The function header is:

def binaryToHex(binaryValue)

Write a test program that prompts the user to enter a binary number and
displays the corresponding hexadecimal value. Use uppercase letters
A, B, C, D, E, F for hex digits.
'''


def main():
    binary = input("Enter a binary number: ")
    print("The hex value is", binaryToHex(binary))


def binaryToHex(binaryValue: str) -> str:
    binary_temp = binaryValue
    hex_value = ""      # Stores the hex value

    # Line up to 4 binary numbers , e.g. 01 would become 0001
    while len(binary_temp) % 4 != 0:
        binary_temp = "0" + binary_temp

    # Go through every 4 numbers of the binary number
    # E.g., 11101100101001 --> 0011 1011 0010 1001
    binary_section = ""
    start_index = 0

    while start_index < len(binary_temp):
        # Look at a section (4 numbers) of the binary number
        binary_section = binary_temp[start_index:start_index + 4]

        # Calculate the decimal number
        # E.g. 1010 -> 1 of 8, 0 of 4, 1 of 2, and 0 of 1 -> 8 + 0 + 2 + 0 = 10
        decimal_num = 0
        for i in range(len(binary_section)):
            if i == 0:
                decimal_num += (int(binary_section[i]) * 8)
            elif i == 1:
                decimal_num += (int(binary_section[i]) * 4)
            elif i == 2:
                decimal_num += (int(binary_section[i]) * 2)
            else:
                decimal_num += (int(binary_section[i]) * 1)

        # Convert the decimal number to the hex value, e.g. 10 -> A
        if decimal_num > 9:
            # 10 -> A, 11 -> B, ... 15 -> F
            hex_value += chr(ord('A') + (decimal_num - 10))
        else:
            # Append 0 - 9 to hex value
            hex_value += str(decimal_num)

        # Go to the next section of 4 numbers in the binary number
        start_index += 4

    # Return the hex value
    return hex_value

main()
