#!/usr/bin/python3
"""Create a square class"""


class Square:
    """I am a big square"""

    def __init__(self, size=0):
        """Create a new Square.
        Args:
            size (int): The size of our new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
