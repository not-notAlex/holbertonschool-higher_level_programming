#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    total = 0
    num = len(argv)
    for i in range(1, num):
        total += int(argv[i])
    print("{:d}".format(total))
