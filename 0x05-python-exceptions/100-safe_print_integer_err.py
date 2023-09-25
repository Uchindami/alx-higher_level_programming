#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        integer = int(value)
        print("{:d}".format(integer))
        return True
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
