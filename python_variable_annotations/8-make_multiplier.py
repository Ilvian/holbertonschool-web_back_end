#!/usr/bin/env python3
'''
Python - Variable Annotations
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    '''
    def mul_num(num: float) -> float:
        return multiplier * num
    return mul_num
