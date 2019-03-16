'''
(Assign grades)

Write a program that reads a list of scores separated by a space in one line
and then assigns grades based on the following scheme:

The grade is A if score is >= best – 10.

The grade is B if score is >= best – 20.

The grade is C if score is >= best – 30.

The grade is D if score is >= best – 40.

The grade is F otherwise.
'''


def main():
    scores = input("Enter scores: ")
    scores_list = [float(x) for x in scores.split(' ')]
    best = max(scores_list)

    for i in range(len(scores_list)):
        score = scores_list[i]
        if score >= (best - 10):
            grade = 'A'
        elif score >= (best - 20):
            grade = 'B'
        elif score >= (best - 30):
            grade = 'C'
        elif score >= (best - 40):
            grade = 'D'
        else:
            grade = 'F'

        print("Student", i, "score is", str(score),
              "and grade is", grade)


if __name__ == "__main__":
    main()
