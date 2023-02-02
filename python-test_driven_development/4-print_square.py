#!/usr/bin/python3
""" function that prints a square with the character # """


def print_square(size):
    """ function that prints a square with the character #

    Args:
        size: an integer, the size of the square.

    Raise:
        TypeError: size must be an integer
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
