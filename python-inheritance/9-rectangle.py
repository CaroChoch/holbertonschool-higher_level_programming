#!/usr/bin/python3
""" BaseGeometry Module : Class Rectangle that inherits from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
     Class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        initialize the size of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return, the following rectangle description: [Rectangle]
        <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
