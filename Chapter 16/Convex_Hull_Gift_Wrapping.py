'''
(Geometry: gift wrapping algorithm for finding a convex hull)

Section 16.16.1 introduced the gift-wrapping algorithm for finding a convex
hull for a set of points. Implement the algorithm using the following function:

# Return the points that form a convex hull

def getConvexHull(points):

Write a test program that prompts the user to enter the points in one line and
displays the points that form a convex hull. Use an IDE to debug the code. As
you debug the code, you will discover that the algorithm overlooked the case
when t1 = t0 and when there is a point that is on the same line from t0 to t1.
When either case happens, replace t1 by this point p if the distance from t0
to p is greater than the distance from t0 to t1.

Sample Run

Enter points: 1 2.4 2.5 2 1.5 34.5 5.5 6 6 2.4 5.5 9

The points are

[[1.0, 2.4], [2.5, 2.0], [1.5, 34.5], [5.5, 6.0], [6.0, 2.4]]

The convex hull is

[[2.5, 2.0], [6.0, 2.4], [5.5, 6.0], [1.5, 34.5], [1.0, 2.4]])
'''


def main():
    data = [float(x) for x in input("Enter points: ").strip().split()]
    points = []

    for coord in range(0, len(data), 2):
        x_coord = data[coord]
        y_coord = data[coord + 1]

        points.append([])
        points[(coord + 1) // 2].append(x_coord)
        points[(coord + 1) // 2].append(y_coord)

    print(points)


main()
