#!/usr/bin/python3
""" An empty class """
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
