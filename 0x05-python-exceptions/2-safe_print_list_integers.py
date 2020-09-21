#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    total = 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            total += 1
            y += 1
        except ValueError:
            y += 1
        except TypeError:
            y += 1
    print()
    return total
