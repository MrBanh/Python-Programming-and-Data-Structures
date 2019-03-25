'''
(Column sorting)

Implement the following function to sort the columns in a two-dimensional list.
A new list is returned and the original list is intact.

def sortColumns(m):

Write a test program that prompts the user to enter a 3 by 3 matrix of numbers
and displays a new column-sorted matrix. Note that the matrix is entered by
rows and the numbers in each row are separated by a space in one line.
'''


def main():
    print("Enter a 3-by-3 matrix row by row: ")
    matrix = []
    for i in range(3):
        s = input().strip().split()
        matrix.append([float(x) for x in s])

    # Obtain the sorted matrix, without changing the original list
    sorted_matrix = sortColumns(matrix)

    # Display result
    print("The column-sorted list is")
    for i in range(3):
        for j in range(3):
            print(sorted_matrix[i][j], end=' ')
        print()


def sortColumns(m: list) -> list:
    lst = m[:]     # Copy the list passed through as an argument

    # Go column-by-column
    for col in range(len(lst[0])):
        # Go through each row in a column
        for row in range(len(lst) - 1):
            # Compare each row in a column to the next row in the same column
            for next_row in range(row + 1, len(lst)):
                # If the value in the next row of the same column is less than
                # current row
                if lst[next_row][col] < lst[row][col]:
                    # Switch the values
                    lst[row][col], lst[next_row][col] = lst[next_row][col], lst[row][col]

    return lst

main()
