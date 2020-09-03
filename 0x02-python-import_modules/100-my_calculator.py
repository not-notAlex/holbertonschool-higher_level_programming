#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == '__main__':
    num = len(argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        func = add
    elif argv[2] == '-':
        func = sub
    elif argv[2] == '*':
        func = mul
    elif argv[2] == '/':
        func = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, func(a, b)))
