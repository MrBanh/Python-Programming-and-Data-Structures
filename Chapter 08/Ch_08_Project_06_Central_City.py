'''
(Central city)

Given a set of cities, the central point is the city that has the shortest
total distance to all other cities. Write a program that prompts the user
to enter the number of the cities and the locations of the cities
(that is, their coordinates), and finds the central city.
Note that the coordinates are entered in one line.
'''


def main():
    s = input("Enter the coordinates of the cities: ").strip().split()
    cities = []

    # Store the coordinates in a list
    for i in range(len(s) // 2):
        cities.append([])       # New row in list

        # Obtain the x- and y-coordinates and append to new row
        for j in range(i * 2, i * 2 + 2):
            cities[i].append(float(s[j]))

    # Get the coordinates of the central city
    x, y = find_central_city(cities)

    # Display the result
    print("The central city is at (" + str(x) + ", " + str(y) + ")")


def find_central_city(lst: list) -> float:
    smallest_distance = 0
    x, y = lst[0][0], lst[0][1]

    # Determine the starting smallest distance
    for other_city in lst:
        smallest_distance += calculate_distance(x, y,
                                                other_city[0], other_city[1])

    # Calculate the distance of each city to the other cities
    for each_city in lst:
        distance = 0
        for other_city in lst:
            distance += calculate_distance(each_city[0], each_city[1],
                                           other_city[0], other_city[1])

        if distance < smallest_distance:
            smallest_distance = distance
            x, y = each_city[0], each_city[1]

    return x, y


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


main()
