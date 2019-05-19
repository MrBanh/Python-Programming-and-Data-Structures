def main():
    n = int(input("Enter a nonnegative integer: "))
    print("The factorial of", n, "is", factorial(n))


def factorial(n):
    return factorial_helper(n, 1)


def factorial_helper(n, result):
    if n == 1:
        return result
    else:
        return factorial_helper(n - 1, n * result)


if __name__ == "__main__":
    main()
