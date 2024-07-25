import math
from typing import Protocol, TypeVar

T = TypeVar("T", bound="Shape")


class Shape(Protocol):
    def calculate_area(self) -> float: ...


class Circle(Shape):
    def __init__(self, radius) -> None:
        if radius is None or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c) -> None:
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
        if self.is_right_triangle():
            return RightTriangle(self.side_a, self.side_b).calculate_area()
        else:
            p = (self.side_a + self.side_b + self.side_c) / 2
            return math.sqrt(
                p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)
            )

    def is_right_triangle(self) -> bool:
        return self.side_a**2 + self.side_b**2 == self.side_c**2


class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        if any(arg is None or arg <= 0 for arg in (width, height)):
            raise ValueError("All sides must be positive numbers.")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class RightTriangle(Rectangle):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    def calculate_area(self) -> float:
        return 0.5 * self.width * self.height


def calculate_shape_area(shape: T) -> float:
    return shape.calculate_area()
