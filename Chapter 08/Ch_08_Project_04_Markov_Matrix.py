'''
(Markov matrix)

An n by n matrix is called a positive Markov matrix if each element is
positive and the sum of the elements in each column is 1. Write the
following function to check whether a matrix is a Markov matrix:

def isMarkovMatrix(m):

Write a test program that prompts the user to enter a 3 by 3 matrix of numbers
and tests whether it is a Markov matrix. Note that the matrix is entered by
rows and the numbers in each row are separated by a space in one line.
'''


def main():
    print("Enter a 3-by-3 matrix row by row: ")
    matrix = []
    for i in range(3):
        s = input().strip().split()
        matrix.append([float(x) for x in s])

    if isMarkovMatrix(matrix):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")


def isMarkovMatrix(m):
    is_markov_matrix = True

    for col_num in range(3):
        total = 0
        for row_num in range(3):
            if m[row_num][col_num] < 0:
                return False

            total += m[row_num][col_num]

        if total != 1:
            return False

    return is_markov_matrix


main()
