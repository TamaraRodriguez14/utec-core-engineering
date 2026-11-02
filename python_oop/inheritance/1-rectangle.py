#!/usr/bin/env python3
"""Module that defines a Rectangle class based on BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated private width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle after validating width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
