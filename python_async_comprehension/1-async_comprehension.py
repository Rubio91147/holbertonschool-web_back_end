#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 0-async_comprehension
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Import async_generator from the previous task and then write a coroutine ca
    lled async_comprehension that takes no arguments.

    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
-------------------------------------------------------------------------------
'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of floats"""

    return [i async for i in async_generator()]
