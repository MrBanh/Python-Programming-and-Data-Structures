'''
Computes and determines the nearest points and finds the closest pair
'''


def nearest_points(points: list) -> int:
    # Indices in points list
    p1, p2 = 0, 1       # Initial two points

    shortest_distance = calculate_distance(points[p1][0], points[p1][1],
                                           points[p2][0], points[p2][1])

    # Compute the distance for every 2 points in the list
    for i in range(len(points)):
        # Compare each points' distance, for example
        # Compares point 1 to point 2, then to point 3, then point 4, etc.
        # Next iteration compares point 2 to point 3, then to point 4, etc.
        for j in range(i + 1, len(points)):
            d = calculate_distance(points[i][0], points[i][1],
                                   points[j][0], points[j][1])

            if d < shortest_distance:
                # New short distance
                p1, p2 = i, j       # Assign the indice of the 2 points
                shortest_distance = d

    # Return the indices of the 2 points with the shortest distance, p1 and p2
    return p1, p2


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
