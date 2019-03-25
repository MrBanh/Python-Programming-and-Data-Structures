'''
(Locate the largest element)

Write the following function that returns the location of the largest
element in a two-dimensional list:

def locateLargest(a):

The return value is a one-dimensional list that contains two elements.
These two elements indicate the row and column indexes of the largest
element in the two-dimensional list.

Write a test program that prompts the user to enter a two-dimensional
list and displays the location of the largest element in the list.
Note that the matrix is entered by rows and the numbers in each row
are separated by a space in one line.
'''


def main():
    num_of_rows = int(input("Enter the number of rows in the list: "))
    matrix = []
    for i in range(num_of_rows):
        row_vals = input("Enter a row: ").strip().split()
        matrix.append([float(x) for x in row_vals])

    # Obtain the row and column of the largest element
    location = locateLargest(matrix)

    # Display the indices of the largest element
    print("The location of the largest element is at (" + str(location[0]) +
          ", " + str(location[1]) + ")")


def locateLargest(a: list) -> list:
    location = [0] * 2      # Initialize for indices of largest element
    largest_element = a[0][0]       # Initialize for largest element value

    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] > largest_element:
                location[0] = row
                location[1] = col
                largest_element = a[row][col]

    return location


main()
