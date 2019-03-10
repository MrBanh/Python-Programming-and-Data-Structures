'''
(Convert milliseconds to hours, minutes, and seconds)

Write a function that converts milliseconds to hours, minutes, and seconds
using the following header:

def convertMillis(millis):

The function returns a string as hours:minutes:seconds.

For example, convertMillis(5500) returns the string 0:0:5,
convertMillis(100000) returns the string 0:1:40, and convertMillis(555550000)
returns the string 154:19:10.

Write a test program that prompts the user to enter a value for milliseconds
and displays a string in the format of hours:minutes:seconds.
'''


def main():
    milliseconds = int(input("Enter time in milliseconds: "))
    print(convertMillis(milliseconds))


def convertMillis(millis: int) -> str:
    time_remaining = millis
    # Convert to hours
    hours = time_remaining // (60 * 60 * 1000)
    time_remaining %= (60 * 60 * 1000)

    # Convert to minutes
    minutes = time_remaining // (60 * 1000)
    time_remaining %= (60 * 1000)

    # Convert to seconds
    seconds = time_remaining // 1000

    return str(hours) + ":" + str(minutes) + ":" + str(seconds)


main()
