#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """ This function removes all characters c and C from a string. """
    new_str = [str for str in my_string if str != 'c' and str != 'C']
    return ("".join(new_str))
