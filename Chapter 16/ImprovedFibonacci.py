def main():
    index = int(input("Enter an index for the Fibonacci number: "))

    # Display
    print(f"Fibonacci number at index {index} is {fib(index)}")


def fib(n):
    f0 = 0
    f1 = 1
    f2 = 1

    if n == 0:
        return f0
    elif n == 1:
        return f1
    elif n == 2:
        return f2

    for _ in range(3, n + 1):
        f0 = f1
        f1 = f2
        f2 = f0 + f1

    return f2


main()
