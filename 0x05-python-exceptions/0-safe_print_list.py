#!/usr/bin/python3
""" A program that prints a given number of item in a list """


def safe_print_list(my_list=[], x=0):
    """ A function takes a list and print x number of items in the list"""
    count, output = 0, ''
    try:
        for i in my_list[:x]:
            output += str(i)
            count += 1
        print(output)
    except Exception as e:
        print(e)
    return count
