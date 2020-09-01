#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = 10
if number < 0:
    mod *= -1
d = number % mod
if d > 0:
    print("Last digit of {:d} is {:d} and is greater than 0".format(number, d))
elif d < 0:
    print("Last digit of {:d} is {:d} and is less than 0".format(number, d))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, d))
