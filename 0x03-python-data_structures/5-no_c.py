#!/usr/bin/python3

def no_c(my_string):
    """Keeping only those that are not 'c' or 'C' """
    return ''.join(char for char in my_string if char not in ('c', 'C'))
