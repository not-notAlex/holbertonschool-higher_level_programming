#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except IndexError as ou:
        print("Exception: {}".format(ou), file=sys.stderr)
        return None
    except TypeError as ou:
        print("Exception: {}".format(ou), file=sys.stderr)
        return None
    except ValueError as ou:
        print("Exception: {}".format(ou), file=sys.stderr)
        return None
    except ZeroDivisionError as ou:
        print("Exception: {}".format(ou), file=sys.stderr)
        return None
