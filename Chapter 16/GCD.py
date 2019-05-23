# Find the gcd for integers m and n
def gcd(m: int, n: int) -> int:
    low, high = (m, n) if m < n else (n, m)
    if high % low == 0:
        return low      # If gcd is one of the integers

    for k in range(high // 2, 0, -1):
        if m % k == 0 and n % k == 0:
            return k


def main():
    m = int(input("Enter the first integer: "))
    n = int(input("Enter the second integer: "))

    print(f'The greatest common divisor for {m} and {n} is {gcd(m, n)}')


main()
