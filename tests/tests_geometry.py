import unittest

import fixtures
from parameterized import parameterized

from geometry.geometry import Circle, Rectangle, RightTriangle, Triangle


class TestGeometry(unittest.TestCase):
    """Tests for geometry.py."""

    @parameterized.expand(fixtures.CORRECT_CIRCLE)
    def test_correct_circle_area(self, radius, result):
        """
        Test that the area of a circle is correct.

        This function uses the fixtures.CORRECT_CIRCLE parameterized fixture to
        provide a set of test cases with correct circle radius and expected
        area values. It creates a Circle object with the given radius and
        asserts that the calculated area is within a small margin of error of
        the expected area.

        Parameters:
            self (TestGeometry): The test case instance.
            radius (int|float): The radius of the circle.
            result (float): The expected area of the circle.

        Returns:
            None
        """
        circle = Circle(radius)
        self.assertAlmostEqual(circle.calculate_area(), result)

    @parameterized.expand(fixtures.NOT_CORRECT_CIRCLE)
    def test_circle_negative_radius(self, radius):
        """
        Test that a ValueError is raised when a negative radius is provided to
        the Circle constructor.

        This function uses the fixtures.NOT_CORRECT_CIRCLE parameterized
        fixture to provide a set of test cases with negative radius values. It
        creates a Circle object with the given radius and asserts that a
        ValueError is raised.

        Parameters:
            self (TestGeometry): The test case instance.
            radius (float): The radius of the circle.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Circle(radius)

    @parameterized.expand(fixtures.CORRECT_TRIANGLE_AREA)
    def test_correct_triangle_area(self, a, b, c, result):
        """
        Test that the area of a triangle is correct.

        This function uses the fixtures.CORRECT_TRIANGLE_AREA parameterized
        fixture to provide a set of test cases with triangle side lengths and
        expected area values. It creates a Triangle object with the given side
        lengths and asserts that the calculated area is within a small margin
        of error of the expected area.

        Parameters:
            self (TestGeometry): The test case instance.
            a (int|float): The length of the first side of the triangle.
            b (int|float): The length of the second side of the triangle.
            c (int|float): The length of the third side of the triangle.
            result (float): The expected area of the triangle.

        Returns:
            None
        """
        triangle = Triangle(a, b, c)
        self.assertAlmostEqual(triangle.calculate_area(), result)

    @parameterized.expand(fixtures.NOT_CORRECT_TRIANGLE)
    def test_triangle_is_not_triangle(self, a, b, c):
        """
        Test that a ValueError is raised when creating a Triangle object with
        incorrect side lengths.

        This function uses the fixtures.NOT_CORRECT_TRIANGLE parameterized
        fixture to provide a set of test cases with incorrect side lengths. It
        creates a Triangle object with the given side lengths and asserts that
        a ValueError is raised.

        Parameters:
            self (TestGeometry): The test case instance.
            a (int|float): The length of the first side of the triangle.
            b (int|float): The length of the second side of the triangle.
            c (int|float): The length of the third side of the triangle.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Triangle(a, b, c)

    @parameterized.expand(fixtures.CORRECT_RIGHT_TRIANGLE_AREA)
    def test_correct_right_triangle_area(self, width, height, result):
        """
        Test that the area of a right triangle is correct.

        This function uses the fixtures.CORRECT_RIGHT_TRIANGLE_AREA
        parameterized fixture to provide a set of test cases with triangle
        width and height values and expected area values. It creates a
        RightTriangle object with the given width and height values and
        asserts that the calculated area is within a small margin of error of
        the expected area.

        Parameters:
            self (TestGeometry): The test case instance.
            width (int|float): The width of the right triangle.
            height (int|float): The height of the right triangle.
            result (float): The expected area of the right triangle.

        Returns:
            None
        """
        right_triangle = RightTriangle(width, height)
        self.assertAlmostEqual(right_triangle.calculate_area(), result)

    @parameterized.expand(fixtures.NOT_CORRECT_RIGHT_TRIANGLE)
    def test_right_triangle_is_not_right_triangle(self, width, height):
        """
        Test that a ValueError is raised when creating a RightTriangle object
        with incorrect width and height values.

        This function uses the fixtures.NOT_CORRECT_RIGHT_TRIANGLE
        parameterized fixture to provide a set of test cases with incorrect
        width and height values. It creates a RightTriangle object with the
        given width and height values and asserts that a ValueError is raised.

        Parameters:
            self (TestGeometry): The test case instance.
            width (int|float): The width of the right triangle.
            height (int|float): The height of the right triangle.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            RightTriangle(width, height)

    @parameterized.expand(fixtures.CORRECT_RECTANGLE_AREA)
    def test_rectangle_area(self, width, height, result):
        """
        Test the area calculation of a rectangle.

        This test case uses parameterized data from the
        `fixtures.CORRECT_RECTANGLE_AREA` fixture to test the
        `calculate_area()` method of the `Rectangle` class.

        Parameters:
            self (TestGeometry): The test case
            width (int|float): The width of the rectangle.
            height (int|float): The height of the rectangle.
            result (float): The expected area of the rectangle.

        Returns:
            None
        """
        rectangle = Rectangle(width, height)
        self.assertAlmostEqual(rectangle.calculate_area(), result)

    @parameterized.expand(fixtures.NOT_CORRECT_RECTANGLE)
    def test_triangle_is_right_triangle(self, width, height):
        """
        Test that a ValueError is raised when creating a Rectangle object
        with incorrect width and height values.

        This function uses the fixtures.NOT_CORRECT_RECTANGLE parameterized
        fixture to provide a set of test cases with incorrect width and height
        values. It creates a Rectangle object with the given width and height
        values and asserts that a ValueError is raised.

        Parameters:
            self (TestGeometry): The test case instance.
            width (int|float): The width of the rectangle.
            height (int|float): The height of the rectangle.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Rectangle(width, height)
