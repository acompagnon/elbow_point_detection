#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Author: Aloyse Compagnon

def detect_elbow(x: list, y: list):
    """Find elbow point in a curve.

    Args:
        x (list): x axis values.
        y (list): y axis values.

    Returns:
        elbow_x: elbow point x axis value.
        elbow_y: elbow point y axis value.
    """
    if not x or not y or len(x) != len(y):
        return None, None

    max_dist = -1
    n = len(x)
    y_first = y[0]
    y_last = y[len(y) - 1]
    avg_fall = (y_last - y_first) / (n - 1)

    coeff = (y_last - y_first) / abs(y_last - y_first)

    for i in range(1, n - 1):
        curr_dist = (coeff * y[i]) - abs(y_first + abs(avg_fall * i))
        if max_dist == -1 or max_dist < curr_dist:
            max_dist = curr_dist
            elbow_x = x[i]
            elbow_y = y[i]

    return elbow_x, elbow_y
