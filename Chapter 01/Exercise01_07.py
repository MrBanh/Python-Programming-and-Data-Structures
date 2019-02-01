"""
(Approximate π)
Write a program that displays the result of
4×(1−1/3+1/5−1/7+1/9−1/11) and
4×(1−1/3+1/5−1/7+1/9−1/11+1/13−1/15)

So calculating the value at each sequence is:
π = 4 * (1/((2 * n - 1) * ((-1) ** (1 - n))),
where n is the nth term of the sequence

For example: n = 8 should show 4 * (- 1 / 15)

-> 4 * (1 / ((2 * 8 - 1) * ((-1) ** (1 - 8))))
-> 4 * (1 / (15 * ((-1) ** -7))
-> 4 * (1 / (15 * (1 / ((-1) ** 7))))
-> 4 * (1 / (15 * (1 / -1)))
-> 4 * (1 / (15 * -1))
-> 4 * (1 / -15)
-> 4 * (- 1 / 15)
"""


# Use recursion to approximate pi based on n-sequence
def approximate_pi(n: int) -> float:
    if n < 0:
        return "n-series cannot be negative"
    elif n == 0:
        return 0
    elif n == 1:
        return 4
    else:
        denominator = 2 * n - 1
        neg_or_pos = (-1) ** (1 - n)
        value_at_n = 4 / (denominator * neg_or_pos)
        return value_at_n + approximate_pi(n - 1)


def show_formula(n: int) -> None:
    if n < 0:
        print("n-series cannot be negative")
    else:
        formula_str = 'π = 4 * ('
        for i in range(1, n + 1):
            denominator = i * 2 - 1
            if i == 1:
                formula_str += '1'
            elif i % 2 == 1:
                formula_str += f' + (1/{denominator})'
            else:
                formula_str += f' - (1/{denominator})'

        formula_str += ') \n==> '
        print(f'\nResult using recursion, where n = {n}')
        print(formula_str, end='')

if __name__ == "__main__":
    n = 6
    show_formula(n)
    print(approximate_pi(n))

    n = 8
    show_formula(n)
    print(approximate_pi(n))

    # Simple solution
    print('\n\nResult with just print, no flexibility')
    print(4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11))
    print(4 * (1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9 - 1 / 11 + 1 / 13 - 1 / 15))
    print()
