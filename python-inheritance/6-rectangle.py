#!/usr/bin/python3
""" Inherits from BaseGeometry """
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class to define a rectangle using base geometry. """
    def __init__(self, width, height):
        """ initialize a new rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
