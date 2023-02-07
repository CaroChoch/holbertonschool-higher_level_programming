#!/usr/bin/python3
""" Class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle
""" Class Square that inherits from Rectangle """


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
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
