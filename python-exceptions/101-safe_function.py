#!/usr/bin/python3


import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as this:
        print("Exception: {}".format(this), file=sys.stderr)
        return None
