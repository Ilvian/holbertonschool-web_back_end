#!/usr/bin/env python3
'''
Python - Async
'''
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    '''
    Function that returns a random delay value
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
