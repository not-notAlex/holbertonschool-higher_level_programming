#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last = len(my_list) - 1
    if last > 0:
        while last >= 0:
            print("{:d}".format(my_list[last]))
            last = last - 1
