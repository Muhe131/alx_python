#!/usr/bin/python3
"""_This module describes about the square_ """


class Square:
    """_Defines a class of square_
    """
    def __init__(self, size = 0):
        """_initializes the new square_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _ if size is not integer_
            ValueError: _if size is less than zero_
        """
        if not isinstance(size, int):
            raise TypeError("size is must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
#my_square = Square(3)
