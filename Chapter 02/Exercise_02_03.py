'''
(Convert feet into meters)
Write a program that reads a number in feet, converts it to meters,
and then displays the result. One foot is 0.305 meters.
'''


def feet_to_meters(feet: float) -> float:
    return feet * 0.305


if __name__ == "__main__":
    feet = float(input('Enter the feets to convert to meters: '))
    print(f'{feet} feet is {feet_to_meters(feet)} meters')
