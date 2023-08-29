#!/usr/bin/env python3

'''Import wait_random from the previous
python file that you’ve written and write an
async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n
times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order
without using sort() because of concurrency.'''


import asyncio
from typing import List

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Function that returns a list
    '''
    l = [get(max_delay) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(l)]
    return finish
