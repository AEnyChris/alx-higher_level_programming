#!/usr/bin/python3
"""This module defines the function find_peak
that returns the peak of an iterable
"""


def find_peak(list_of_integers):
    """returns the peak or max value of a list

    Argument:
            list_of_integers (list): a list or iterable
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
