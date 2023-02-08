#!/usr/bin/python3
""" Class MyInt that inherits from int """


class MyInt(int):
    """
    Inherits from int.
    MyInt has == and != operators inverted
    """

    def __eq__(self, value):
        """
        Magic method equals
        """
        return int(self) != value

    def __ne__(self, value):
        """
        Magic method not equals
        """
        return int(self) == value
