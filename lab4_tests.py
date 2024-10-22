import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[5], [], [8, 9]]
        result = lab4.first_element(input)
        expected = [5, 8]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        points = [data.Point(1, 2), data.Point(3, 4)]
        result = lab4.x_coordinates(points)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        points = [data.Point(-1, -2), data.Point(0, 0), data.Point(5, 7)]
        result = lab4.x_coordinates(points)
        expected = [-1, 0, 5]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        points = [data.Point(1, 2), data.Point(-1, -2), data.Point(3, 4)]
        result = lab4.are_in_positive_quadrant(points)
        expected = [data.Point(1, 2), data.Point(3, 4)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        points = [data.Point(0, 0), data.Point(-1, 1), data.Point(2, -2)]
        result = lab4.are_in_positive_quadrant(points)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(3, 4)
        result = lab4.distance(p1, p2)
        expected = 5.0  # Euclidean distance between (0,0) and (3,4) is 5
        self.assertEqual(expected, result)

    def test_distance_2(self):
        p1 = data.Point(-1, -1)
        p2 = data.Point(4, 5)
        result = lab4.distance(p1, p2)
        expected = 7.810249675906654  # Calculated distance
        self.assertAlmostEqual(expected, result, places = 6)

    # Part 5
    def test_manhattan_distance_1(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(3, 4)
        result = lab4.manhattan_distance(p1, p2)
        expected = 7  # Manhattan distance = |3 - 0| + |4 - 0|
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        p1 = data.Point(-1, -1)
        p2 = data.Point(4, 5)
        result = lab4.manhattan_distance(p1, p2)
        expected = 11  # Manhattan distance = |4 - (-1)| + |5 - (-1)|
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        points = [data.Point(3, 4), data.Point(6, 8)]
        result = lab4.distance_all(points)
        expected = [5.0, 10.0]  # Distances from origin (0,0)
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        points = [data.Point(0, 0), data.Point(-3, -4)]
        result = lab4.distance_all(points)
        expected = [0.0, 5.0]  # Distance to origin (0,0)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
