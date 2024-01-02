#!/usr/bin/env python3
'''
Python - Async
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function that returns a list of delays
    '''
    delayed_tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delayed_tasks.append(task)
    result_list = await asyncio.gather(*delayed_tasks)
    return sorted(result_list)

