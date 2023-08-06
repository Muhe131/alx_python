#!/usr/bin/python3
""" A base class for the upcoming projects """


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """  initializes id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
