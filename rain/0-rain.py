#!/usr/bin/python3
"""
Module to calculate the amount of rainwater retained after it rains.
"""


def rain(walls):
    """
    Calculate the number of square units of water retained after it rains.

    Arguments:
    walls -- list of non-negative integers representing wall heights

    Returns:
    Integer indicating the total amount of rainwater retained.
    """
    if not walls:
        return 0

    left_index, right_index = 0, len(walls) - 1
    max_left, max_right = 0, 0
    total_water = 0

    while left_index < right_index:
        if walls[left_index] <= walls[right_index]:
            max_left = max(max_left, walls[left_index])
            total_water += max_left - walls[left_index]
            left_index += 1
        else:
            max_right = max(max_right, walls[right_index])
            total_water += max_right - walls[right_index]
            right_index -= 1

    return total_water
