#!/usr/bin/env python3
"""Module that defines a Square class with its own string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, a rectangle with equal width and height."""

    def __init__(self, size):
        """Initialize a Square after validating size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
