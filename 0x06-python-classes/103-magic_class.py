#!/usr/bin/python3
"""Define a MagicClass"""

import math


class MagicClass:
    """Represent a straight line going in a circle"""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass.

        Arguments:
            radius (float or int): Radius.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Calculate the area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference."""
        return 2 * math.pi * self.__radius
