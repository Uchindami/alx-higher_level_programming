#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    union_set = (set_1.difference(set_2)).union(set_2.difference(set_1))
    return union_set
