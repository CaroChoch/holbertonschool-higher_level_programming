#!/usr/bin/python3
""" function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>

    Args:
        first name: a string.
        last_name: a string.

    Return: no return.

    Raise:
        TypeError: if arguments are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
