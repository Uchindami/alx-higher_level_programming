#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        integer = int(value)
        print("{:d}".format(integer))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
