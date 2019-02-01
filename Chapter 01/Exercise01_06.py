"""
(Summation of a series)
Write a program that displays the result of
1+2+3+4+5+6+7+8+9
"""


# Use recursion to calculate summation of a series
def summation_series(series: int) -> int:
    if series == 1 or series == 0:
        return series
    else:
        return series + summation_series(series - 1)


if __name__ == "__main__":
    print(summation_series(9))      # Pass in the highest value in a sequence
