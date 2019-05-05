'''
(Process scores in a text file)

Suppose that a text file contains an unspecified number of scores.
Write a program that prompts the user to enter the filename and reads the
scores from the file and displays their total and average. Scores are
separated by blanks. Your program should prompt the user to enter a filename.
'''


def main():
    filename = input("Enter a filename: ").strip()
    total = 0
    count = 0

    # Open the filename
    with open(filename, 'r') as file:
        score_list = file.read().split()

    for score in score_list:
        count += 1
        total += float(score)

    avg = total / count

    # Print results
    print("There are", count, "scores")
    print("The total is", total)
    print("The average is", avg)

main()
