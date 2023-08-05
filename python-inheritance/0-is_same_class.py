#!/usr/bin/python3
"""_Checks if the object is an instance of a class_"""
def is_same_class(obj, a_class):
    """_Returns True if the object is exactly an instance of the specified class ; otherwise False."""
    return (type(obj) == a_class)