#!/usr/bin/python3
""" An empty class """
class BaseGeometryMetaClass(type):
     """ defines empty class """
     def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    pass

""" class BaseGeometry:
     def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class MuheClass(metaclass=BaseGeometryMetaClass):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
pass """