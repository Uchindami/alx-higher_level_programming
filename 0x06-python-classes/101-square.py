#!/usr/bin/python3
"""Back to squares."""


class Square:
    """Write a class Square that defines a square
        by: (based on 6-square.py)."""
    def __init__(self, size=0, position=(0, 0)):
        """
        start a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square as (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns Area"""
        return self.__size ** 2

    def my_print(self):
        """#chars for squares."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the print() representation of a Square."""
        output = ""
        if self.__size != 0:
            output += "\n" * self.__position[1]
            for _ in range(self.__size):
                output += " " * self.__position[0] + "#" * self.__size
                if _ != self.__size - 1:
                    output += "\n"
        return output
