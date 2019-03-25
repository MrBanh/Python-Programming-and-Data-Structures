import Nearest_Points_Example


def main():
    num_of_points = int(input("Enter the number of points: "))

    # Create a list to store points
    points = []
    for i in range(num_of_points):
        s = input(f"Enter x- and y-coordinates of point {i + 1}: ")
        point = [float(x) for x in s.split()]       # Convert to a list
        points.append(point)        # Append the point to list of points

    # Get the indices of the 2 points with the shortest distance
    p1, p2 = Nearest_Points_Example.nearest_points(points)

    # Display result
    print(f"The closest two points are ({points[p1][0]}, {points[p1][1]})" +
          f" and ({points[p2][0]}, {points[p2][1]})")


main()
