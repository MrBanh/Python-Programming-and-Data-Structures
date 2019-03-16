'''
(Statistics: compute deviation)
computes the standard deviation of numbers. This exercise uses a
different but equivalent formula to compute the standard deviation
of n numbers.

mean = (x1 + x2 + x3 + ... + xn) / n
deviation = SQROOT of ( ( sum of ((xi - mean) ** 2) for i = 1 to n ) / (n - 1) )

Write a test program that prompts the user to enter a list of
numbers in one line and displays the mean and standard deviation
'''


def main() -> None:
    nums = input("Enter numbers: ")
    nums = [float(num) for num in nums.split(' ')]
    print("The mean is", mean(nums))
    print("The standard deviation is", deviation(nums))


def deviation(nums: list) -> float:
    sums = 0
    mean_val = mean(nums)
    for i in range(len(nums)):
        sums += (nums[i] - mean_val) ** 2

    return (sums / (len(nums) - 1)) ** 0.5


def mean(nums: list) -> float:
    return (sum(nums) / len(nums))


if __name__ == "__main__":
    main()
