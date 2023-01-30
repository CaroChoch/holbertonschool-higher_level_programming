#!/usr/bin/python3
"""Define a class Square by private instance attribute size."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): Size of the new square. private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area of a square.
        """
        return self.__size ** 2
