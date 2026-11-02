#!/usr/bin/env python3
"""Module that defines a BaseGeometry class for geometric shapes."""


class BaseGeometry:
    """Base class that provides shared behavior for geometric shapes."""

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Raises TypeError if value is not an integer and
        ValueError if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
