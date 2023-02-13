#!/usr/bin/python3
""" Square Class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.width = self.height = value
