#!/usr/bin/python3
""" class Square that inherits from Rectangle (9-rectangle.py) """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle (9-rectangle.py)
    """

    def __init__(self, size):
        """
        size must be private. No getter or setter.
        size must be a positive integer, validated by integer_validator.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area() method must be implemented.
        """

        return self.__size * self.__size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
