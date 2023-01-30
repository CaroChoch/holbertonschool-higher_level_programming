#!/usr/bin/python3
"""Define a class Square by private instance attribute size."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): Size of the new square. private instance attribute.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area of a square.
        """
        return self.__size ** 2
