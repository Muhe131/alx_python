#!/usr/bin/python3
""" Checks if an object is inherited """
def inherits_from(obj, a_class):
    return (issubclass(type(obj), a_class) and type(obj) != a_class )