#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    num = len(argv)
    d = 1
    if num == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(num - 1))
        while d < num:
            print("{:d}: {:s}".format(d, argv[d]))
            d += 1
