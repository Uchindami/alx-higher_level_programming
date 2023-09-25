#!/usr/bin/python3

def safe_print_integer(value):
    """eh guys commenting is job on its own"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
