#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """A new Square.

        Args:
            size (int): passed size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """since Size is private use getter to get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """since Size is private use setter to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of our beautiful square."""
        return self.__size * self.__size
