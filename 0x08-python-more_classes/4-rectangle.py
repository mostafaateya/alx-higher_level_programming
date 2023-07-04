#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """ Start a new rectangle
        args:
        width: init
        height: init

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the are of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the rectangle
        Represent the rectangle with #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        a = []
        for x in range(self.__height):
            [a.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                a.append("\n")
        return ("".join(a))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        a = "Rectangle(" + str(self.__width)
        a += ", " + str(self.__height) + ")"
        return (a)
