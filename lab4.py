import data

# Write your functions for each part in the space below.

# Part 1

def first_element(nested_list: list[list[int]]) -> list[int]:
    """
    Purpose:
    - Return a list containing the first element of each non-empty list in the input list of lists.

    Input:
    - A list of lists of integers, 'nested_list'.

    Output:
    - A list of integers representing the first element of each non-empty nested list.

    Data Representation:
    - The input is a list of lists of integers. The output is a list of integers.

    Function Template:
    def first_element(nested_list: list[list[int]]) -> list[int]:
    """
    return [lst[0] for lst in nested_list if lst]

# Part 2
def x_coordinates(points: list[data.Point]) -> list[float]:
    """
    Purpose:
    - Return a list of the x-coordinates of each Point object in the input list.

    Input:
    - A list of 'Point' objects, 'points'.

    Output:
    - A list of floats representing the x-coordinates of the points.

    Data Representation:
    - The input is a list of 'Point' objects (defined in data.py). The output is a list of floats (x-coordinates).

    Function Template:
    def x_coordinates(points: list[data.Point]) -> list[float]:
    """
    return [point.x for point in points]

# Part 3
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    """
    Purpose:
    - Return a list of points that are in the first quadrant of the Cartesian plane (x > 0 and y > 0).

    Input:
    - A list of 'Point' objects, 'points'.

    Output:
    - A list of 'Point' objects that are in the first quadrant.

    Data Representation:
    - The input is a list of 'Point' objects. The output is a list of 'Point' objects (filtered based on positive x and y coordinates).

    Function Template:
    def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    """
    return [point for point in points if point.x > 0 and point.y > 0]

# Part 4
import math

def distance(p1: data.Point, p2: data.Point) -> float:
    """
    Purpose:
    - Return the Euclidean distance between two points.

    Input:
    - Two 'Point' objects, 'p1' and 'p2'.

    Output:
    - A float representing the Euclidean distance between the two points.

    Data Representation:
    - The input consists of two 'Point' objects, each with x and y coordinates. The output is a float representing the Euclidean distance.

    Function Template:
    def distance(p1: data.Point, p2: data.Point) -> float:
    """
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Part 5
def manhattan_distance(p1: data.Point, p2: data.Point) -> float:
    """
    Purpose:
    - Return the Manhattan distance between two points.

    Input:
    - Two 'Point' objects, 'p1' and 'p2'.

    Output:
    - A float representing the Manhattan distance between the two points.

    Data Representation:
    - The input consists of two 'Point' objects, each with x and y coordinates. The output is a float representing the Manhattan distance.

    Function Template:
    def manhattan_distance(p1: data.Point, p2: data.Point) -> float:
    """
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Part 6
def distance_all(points: list[data.Point]) -> list[float]:
    """
    Purpose:
    - Return a list of distances from the origin (0, 0) to each point in the input list.

    Input:
    - A list of 'Point' objects, 'points'.

    Output:
    - A list of floats representing the Euclidean distance from the origin to each point.

    Data Representation:
    - The input is a list of 'Point' objects. The output is a list of floats representing the Euclidean distances.

    Function Template:
    def distance_all(points: list[data.Point]) -> list[float]:
    """
    origin = data.Point(0, 0)
    return [distance(origin, point) for point in points]
