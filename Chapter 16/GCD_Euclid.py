def gcd(m: int, n: int) -> int:
    # base case, if m % n is 0, the gcd is n
    if m % n == 0:
        return n
    else:
        # Otherwise, gcd(m, n) is gcd(n, m % n)
        return gcd(n, m % n)


def main():
    m = int(input("Enter the first integer: "))
    n = int(input("Enter the second integer: "))

    print(f'The greatest common divisor for {m} and {n} is {gcd(m, n)}')


main()
