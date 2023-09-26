#!/usr/bin/python3
"""Create a square class"""


class Square:
    """I am a big square"""

    def __init__(self, size):
        """Create a new Square.
        Args:
            size (int): The size of our new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
