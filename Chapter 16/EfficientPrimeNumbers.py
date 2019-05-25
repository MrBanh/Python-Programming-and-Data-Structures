def main():
    n = int(input("Find all prime numbers <= n, enter n: "))

    # List to hold prime numbers
    lst = []

    NUMBER_PER_LINE = 10        # Display 10 numbers per line
    count = 0       # Count the number of prime numbers
    number = 2      # A Number to be tested for prime
    square_root = 1     # Check whether number <= square_root

    print("The prime numbers are:")

    # Repeat and find prime numbers
    while number <= n:
        # Assume it is prime
        is_prime = True

        if square_root * square_root < number:
            square_root += 1

        # Test for prime
        k = 0
        while k < len(lst) and lst[k] <= square_root:
            if number % lst[k] == 0:        # If true, not prime
                is_prime = False
                break
            k += 1

        if is_prime:
            count += 1      # Increase the count
            lst.append(number)
            if count % NUMBER_PER_LINE == 0:
                # Print the number and advance to new line
                print(number)
            else:
                print(str(number) + " ", end='')

        # Check if next number is prime
        number += 1

    print("\n" + str(count) + " prime(s) less tha or equal to " + str(n))


main()
