#!/usr/bin/env python3
"""Module that defines a Square class with a validated private size."""


class Square:
    """Represent a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Raises TypeError if size is not an integer and
        ValueError if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
