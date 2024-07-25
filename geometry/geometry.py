import math
from typing import Protocol, TypeVar

T = TypeVar("T", bound="Shape")


class Shape(Protocol):
    def calculate_area(self) -> float: ...


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        """
        Initialize a Circle object with the given radius.

        Args:
            radius (int | float): The radius of the circle. Must be a positive
            number.

        Raises:
            ValueError: If the radius is None or less than or equal to 0.

        Returns:
            None
        """
        if radius is None or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def calculate_area(self) -> float:
        """
        Calculate the area of a circle.

        This function takes no parameters and returns the area of a circle.
        The area is calculated using the formula:
        area = π * radius^2

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(
        self, side_a: int | float, side_b: int | float, side_c: int | float
    ) -> None:
        """
        Initializes a Triangle object with the given side lengths.

        Args:
            side_a (int | float): The length of the first side of the triangle.
            side_b (int | float): The length of the second side of the
            triangle.
            side_c (int | float): The length of the third side of the triangle.

        Raises:
            ValueError: If any of the side lengths are None or less than or
            equal to 0.
            ValueError: If the given side lengths cannot form a valid triangle.

        Returns:
            None
        """
        if any(arg is None or arg <= 0 for arg in (side_a, side_b, side_c)):
            raise ValueError("All sides must be positive numbers.")
        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("There is no triangle with such sides.")
        sides = sorted([side_a, side_b, side_c])
        self.side_a = sides[0]
        self.side_b = sides[1]
        self.side_c = sides[2]

    def calculate_area(self) -> float:
        """
        Calculate the area of the triangle.

        This method calculates the area of the triangle using Heron's formula
        if the triangle is not a right triangle.
        If the triangle is a right triangle, it creates a new RightTriangle
        object with the same side lengths and calls
        its calculate_area() method to calculate the area.

        Returns:
            float: The area of the triangle.
        """
        if self.is_right_triangle():
            return RightTriangle(self.side_a, self.side_b).calculate_area()
        else:
            p = (self.side_a + self.side_b + self.side_c) / 2
            return math.sqrt(
                p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)
            )

    def is_right_triangle(self) -> bool:
        """
        Check if the triangle is a right triangle.

        Returns:
            bool: True if the triangle is a right triangle, False otherwise.
        """
        return self.side_a**2 + self.side_b**2 == self.side_c**2


class Rectangle(Shape):
    def __init__(self, width: int | float, height: int | float) -> None:
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int | float): The width of the rectangle.
            height (int | float): The height of the rectangle.

        Raises:
            ValueError: If either width or height is None or less than or
            equal to 0.

        Returns:
            None
        """
        if any(arg is None or arg <= 0 for arg in (width, height)):
            raise ValueError("All sides must be positive numbers.")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        This method calculates the area of the rectangle by multiplying the
        width and height.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height


class RightTriangle(Rectangle):
    def __init__(self, width: int | float, height: int | float) -> None:
        """
        Initializes a new instance of the class.

        Args:
            width (int | float): The width of the object.
            height (int | float): The height of the object.

        Returns:
            None
        """
        super().__init__(width, height)

    def calculate_area(self) -> float:
        """
        Calculate the area of the right triangle.

        This method calculates the area of the right triangle by multiplying
        half of the width by the height.

        Returns:
            float: The area of the right triangle.
        """
        return 0.5 * self.width * self.height


def calculate_shape_area(shape: T) -> float:
    """
    Calculate the area of a shape.

    Args:
        shape (T): The shape object for which the area needs to be calculated.

    Returns:
        float: The area of the shape.
    """
    return shape.calculate_area()
