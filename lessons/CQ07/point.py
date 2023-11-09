"""CQ07."""

from __future__ import annotations

__author__ = "730525294"


class Point:
    """Represents a point in 2D space."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Assigns x, y as the initial values for attributes."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutates a Point."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Creates a new Point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Print out x,y."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Create a new point with a factor of input point."""
        new_point: Point = self
        new_point.x *= factor
        new_point.y *= factor
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Create a new point with a factor of input point."""
        new_point: Point = self
        new_point.x += factor
        new_point.y += factor
        return new_point