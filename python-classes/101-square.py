#!/usr/bin/python3
"""Define a class Square by private instance attribute size."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): Size of the new square. private instance attribute.
            position (int, int): Position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the current square area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Defines the print() representation of a Square."""
        square = []
        if self.__size == 0:
            square.append()
        else:
            for i in range(self.__position[1]):
                square.append("")
            for row in range(self.__size):
                square.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(square)
