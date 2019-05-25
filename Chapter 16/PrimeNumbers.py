from math import sqrt


def main():
    n = int(input("Find all prime numbers <= n, enter n: "))
    NUMBER_PER_LINE = 10        # Display 10 numbers per line
    count = 0       # Count the number of prime numbers
    number = 2      # A Number to be tested for prime

    print("The prime numbers are:")

    square_root = 1
    # Repeat and find prime numbers
    while number <= n:
        # Assume it is prime
        is_prime = True

        if square_root * square_root < number:
            square_root += 1

        for divisor in range(2, square_root + 1):
            # If number is not a prime
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1      # Increase the count

            if count % NUMBER_PER_LINE == 0:
                # Print the number and advance to new line
                print(" " + str(number))
            else:
                print(" " + str(number), end='')

        # Check if next number is prime
        number += 1

    print("\n" + str(count) + " prime(s) less tha or equal to " + str(n))


main()
