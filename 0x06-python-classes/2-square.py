#!/usr/bin/python3
"""The Square class"""


class Square:
    """
    A class to define squares
    Attributes: 
         __size (int) > 0: the size of the sides of the square
    """

    def __init__(self, size=0):
        """
        instance constructor with test for attr size
        Arg:
            size (int) > 0: the size of the sides of the square
        Return:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >0")
        else:
            self.__size = size
