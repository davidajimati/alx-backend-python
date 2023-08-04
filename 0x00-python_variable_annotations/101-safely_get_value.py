#!/usr/bin/env python3
"""adding annotations to the function below"""


from typing import Mapping, Any, Optional, Union, TypeVar
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """returns the key of every item in the dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
