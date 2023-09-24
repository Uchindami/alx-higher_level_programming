#!/usr/bin/python3

def element_at(my_list, idx, element):
    """ Replace an element from a list like in C """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)

