'''
(Algebra: add two matrices)
Write a function to add two matrices. The header of the function is:

def addMatrix(a, b):

In order to be added, the two matrices must have the same dimensions
and the same or compatible types of elements. Let c be the resulting matrix.

Each element cij is  aij+bij

a11 a12 a13     b11 b12 b13   a11+b11  a12+b12  a13+b13
a21 a22 a23  +  b21 b22 b23 = a21+b21  a22+b22  a23+b23
a31 a32 a33     b31 b32 b33   a31+b31  a32+b32  a33+b33
'''


def main():
    matrix1 = []
    matrix2 = []
    row_num = -1

    m1 = input("Enter a 3-by-3 matrix1: ").strip().split()
    m2 = input("Enter a 3-by-3 matrix2: ").strip().split()

    for i in range(9):
        if i % 3 == 0:
            matrix1.append([])      # Create a row
            matrix2.append([])      # Create a row
            row_num += 1        # Go to next row

            # Add values from input to the matrixes
            matrix1[row_num].append(float(m1[i]))
            matrix2[row_num].append(float(m2[i]))

        else:
            matrix1[row_num].append(float(m1[i]))
            matrix2[row_num].append(float(m2[i]))

    c = addMatrix(matrix1, matrix2)
    for row in range(3):
        # print first matrix
        for col in range(3):
            print(matrix1[row][col], end=' ')

        print(" +   " if row == 1 else "     ", end=' ')

        # print second matrix
        for col in range(3):
            print(matrix2[row][col], end=' ')

        print(" =   " if row == 1 else "     ", end=' ')

        # print resulting matrix
        for col in range(3):
            print(c[row][col], end=' ')

        print()


def addMatrix(a: list, b: list) -> list:
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j] + b[i][j])

    return c

main()
