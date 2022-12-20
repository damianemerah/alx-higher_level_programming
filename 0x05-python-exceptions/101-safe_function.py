#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        results = fct(*args)
    except Exception as e:
        results = None
        print("Exception: {}".format(e), file=sys.stderr)
    return results
