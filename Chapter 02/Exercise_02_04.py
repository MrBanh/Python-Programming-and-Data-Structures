'''
(Convert pounds into kilograms)
Write a program that converts pounds into kilograms.
The program prompts the user to enter a value in pounds,
converts it to kilograms, and then displays the result.
One pound is 0.454 kilograms.
'''


def lb_to_kg(pounds: float) -> float:
    return pounds * 0.454


if __name__ == "__main__":
    pounds = float(input('Ente a number in pounds: '))
    print(f'{pounds} pounds is {lb_to_kg(pounds)} kilograms')
