#!/usr/bin/python3
"""
module for task 6
"""


def find_peak(list_of_integers):
    """
    finds a peak in unsorted list
    """
    if not list_of_integers:
        return None
    size = len(list_of_integers)
    nums = list_of_integers
    if size == 1:
        return nums[0]
    if size == 2:
        if nums[0] > nums[1]:
            return nums[0]
        else:
            return nums[1]
    i = int(size / 2)
    while True:
        if i == 0 or i == (size - 1):
            return nums[i]
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return nums[i]
        if nums[i + 1] > nums[i]:
            i = int((i + size) / 2)
        else:
            i = int(i / 2)
