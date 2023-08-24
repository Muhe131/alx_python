#!/usr/bin/python3
"""Checks if the object is inherited or same class"""
def is_kind_of_class(obj, a_class):
    """Returns True if the object an instance of, or if the object is an instance of a class that inherited from ; otherwise False."""
    return (isinstance(obj, a_class))