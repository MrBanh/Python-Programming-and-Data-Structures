def main():
    n = int(input("Enter n to find the fibonacci value at n: "))
    print("The fibonacci value at", n, "is", fib(n))


def fib(n):
    return fib_helper(n, 1, 0)


def fib_helper(n, next, result):
    if n <= 0:
        return result
    else:
        return fib_helper(n - 1, next + result, next)


if __name__ == "__main__":
    main()