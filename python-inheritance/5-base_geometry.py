#!/usr/bin/python3
""" Base Geometry """
class BaseGeometryMetaClass(type):
    """ defines base geometry class """
    def __dir__(cls):
         return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """ defines empty class """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    def area(self):
        """ method not implemented yet """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Validates a value as an integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
