#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    """ returns sum of elements in mxd_list"""
    sum: float = 0
    for i in range(len(mxd_lst)):
        sum += mxd_lst[i]
    return sum
