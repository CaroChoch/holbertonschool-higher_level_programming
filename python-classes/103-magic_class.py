#!/usr/bin/python3
""" Class  MagicClass """

import math


class MagicClass:

    """ Defines a circle
    Args:
        radius (int, float) = Circle radius
    """

    __radius = None

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):

        """ Calculates the area of the circle """

        return (self.__radius ** 2) * math.pi

    def circumference(self):

        """ Calculates the circumference of the circle """

        return 2 * math.pi * self.__radius
