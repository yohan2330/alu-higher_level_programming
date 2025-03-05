#!/usr/bin/python3
# 2-square.py
"""Module defining a Square class.

This module provides a Square class with size validation.
"""

class Square:
    """Class representing a square."""
    def __init__(self, size=0):
        """Initialize a Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
