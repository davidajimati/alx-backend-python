#!/usr/bin/env python3
"""returns values with appropriate types"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns element length"""
    return [(i, len(i)) for i in lst]
