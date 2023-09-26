#!/usr/bin/python3
"""Tired of this square BS"""


class Square:
    def __init__(self, side_length=0):
        """
        More squares people.

        Args:
            side_length (int): The Provided length.
        """
        self.side_length = side_length

    @property
    def side_length(self):
        """Get or set the length of each side of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        elif value < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__side_length ** 2

    def __eq__(self, other):
        """ == based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """ != based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """ < based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """<=  based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """ > comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= comparison."""
        return self.area() >= other.area()
