#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    num = len(argv)
    d = 1
    if num == 1:
        print("0 arguments.")
    elif num == 2:
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(num - 1))
        while d < num:
            print("{:d}: {:s}".format(d, argv[d]))
            d += 1
