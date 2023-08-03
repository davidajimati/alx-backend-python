#!/usr/bin/env python3
"""takes a float and returns a function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multiplier"""
    def multiply(x: float) -> float:
        """Returns the multiplicated x"""
        return (x * multiplier)
    return (multiply)
