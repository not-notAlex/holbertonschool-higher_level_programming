#!/usr/bin/python3
import add_0
if __name__ == '__main__':
    add = add_0.add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
