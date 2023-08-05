#!/usr/bin/python3
""" An empty class """
class BaseGeometry:
    """ defines base geometry class """
    def area(self):
        """ method not implemented yet """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Validates a value as an integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
