#!/usr/bin/env python3
'''Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer
max_delay and returns a asyncio.Task.'''


import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay):
    return asyncio.create_task(wait_random(max_delay))


async def test(max_delay: int):
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)
    asyncio.run(test(5))
