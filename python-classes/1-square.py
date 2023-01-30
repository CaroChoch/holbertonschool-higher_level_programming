#!/usr/bin/python3
"""Define a class Square by private instance attribute size."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): Size of the new square. private instance attribute.
        """
        self.__size = size
