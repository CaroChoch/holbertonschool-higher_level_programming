#!/usr/bin/python3
""" Function add_attribute hat adds
a new attribute to an object if it’s possible
"""


def add_attribute(self, name, value):
    """
    Adds new attribute to an object if it's possible
    """
    if hasattr(self, '__dict__'):
        setattr(self, name, value)
    else:
        raise TypeError("can't add new attribute")
