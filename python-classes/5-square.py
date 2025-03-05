#!/usr/bin/python3
# 5-square.py
"""Square module."""

class Square:
    """Square class."""
    def __init__(self, size=0):
        """Init size."""
        self.size = size

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get area."""
        return self.__size ** 2

    def my_print(self):
        """Print square."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
