#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """ returns sum of input_list elements"""
    return (sum(input_list))