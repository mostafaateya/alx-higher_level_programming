#!/usr/bin/python3
"""Class rectangel"""


class Rectangle:
    """Define a class"""

    def __init__(self, width=0, height=0):
        """Start a new rectangle
        Args:
        width: int
        height: init

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the rectangel"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the rectangle
        represent rectangel with #
        """
        if self.width == 0 or self.height == 0:
            return ""

        a = []
        for x in range(self.height):
            [a.append('#') for y in range(self.width)]
            if x != self.height - 1:
                a.append("\n")
        return "".join(a)
