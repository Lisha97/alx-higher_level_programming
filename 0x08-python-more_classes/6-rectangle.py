#!/usr/bin/python3

"""
Definition of a class Rectangle
"""


class Rectangle:
    """
    define class Rectangle with some attributes: width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2*(self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        x = ''
        for i in range(self.__height):
            x += str('#' * self.__width) + '\n'
        x = x[:-1]
        return x

    def __repr__(self):
        return('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
