#!/usr/bin/env python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
