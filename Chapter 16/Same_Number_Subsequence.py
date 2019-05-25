'''
(Same-number subsequence)

Write an O(n) program that prompts the user to enter a sequence of integers in
one line and finds longest subsequence with the same number.

Sample Run
Enter a series of numbers: 2 4 4 8 8 8 8 2 4 4 0

The longest same number sequence starts at index 3 with 4 values of 8
'''


def main():
    nums = [int(x) for x in input("Enter a series of numbers: ").strip().split()]
    index, count, num = same_number_sequence(nums)
    print("The longest same number sequence starts at index", index,
          "with", count, "values of", num)


def same_number_sequence(nums):
    # Keeps track of # of occurrence of a number in a subsequence
    highest_count = 0
    # Tracks the index of where the highest subsequence number first appears
    index_of_subsequence = 0
    # Starting count of number in nums
    count = 1

    # Loop through nums: O(n)
    for i in range(1, len(nums)):
        # If num in nums matches the previous num in nums
        # -> subsequence continues
        if nums[i] == nums[i - 1]:
            # Add to count to keep track of occurrence
            count += 1

        # num in nums does not match previous num in nums
        # -> subsequence is broken
        else:
            # Determine if the current subsequence is longest
            # Compare count of current subsequence to highest count
            if count > highest_count:
                highest_count = count
                index_of_subsequence = i - highest_count
                count = 1

    return (index_of_subsequence, highest_count, nums[index_of_subsequence])

main()
