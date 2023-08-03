#!/usr/bin/env python3
"""takes variables, returns a tuple"""

import typing


def to_kv(k: str, v: typing.Union[int | float]) -> typing.Tuple[str, float]:
    """returns a float value from k and v"""
    return ((k, v*v))
