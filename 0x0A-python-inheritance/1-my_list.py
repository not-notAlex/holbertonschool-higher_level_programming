#!/usr/bin/python3
"""
module for 1-my_list
"""


class MyList(list):
    """
    sorted list
    """
    def print_sorted(self):
        """
        sorts the list
        """
        print(sorted(self))
