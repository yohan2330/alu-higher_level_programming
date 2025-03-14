#!/usr/bin/python3
# 3-square.py
"""Square class module."""

class Square:
    """Square with size."""
    def __init__(self, size=0):
        """Init with size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area."""
        return self.__size ** 2
