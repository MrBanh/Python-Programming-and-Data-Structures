'''
(Sum elements column by column)

Write a function that returns the sum of all the elements in a specified
column in a matrix using the following header:

def sumColumn(m, columnIndex):

Write a test program that reads a 3 × 4 matrix and
displays the sum of each column.
'''


def main():
    matrix = []
    for row in range(3):
        s = input("Enter a 3-by-4 matrix row " + str(row) + ": ").strip()
        matrix.append([float(x) for x in s.split()])

    for col in range(4):
        print("Sum of the elements for column " + str(col) + " is",
              sumColumn(matrix, col))


def sumColumn(m: list, columnIndex: int) -> float:
    total = 0
    for row_num in range(3):
        total += m[row_num][columnIndex]

    return total


main()
