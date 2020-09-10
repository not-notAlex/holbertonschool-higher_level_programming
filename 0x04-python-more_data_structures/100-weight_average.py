#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    if my_list is None:
        return 0
    for i in my_list:
        num += (i[0] * i[1])
    for i in my_list:
        den += i[1]
    return float(num / den)
