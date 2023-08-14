#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    This function finds the biggest integer of a list
    """
    if len(my_list) == 0:
        return (None)
    my_list.sort()
    return (my_list[-1])
