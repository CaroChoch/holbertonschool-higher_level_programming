#!/usr/bin/python3
""" Function that adds 2 integers """


def add_integer(a, b=98):
    """ function that adds 2 integers or floats.

    Args:
        a: first integer or float to add.
        b: second integer or float to add.

    Return: an integer: the sum of a and b.

    Raise: TypeError if a or b aren't integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    return a + b
