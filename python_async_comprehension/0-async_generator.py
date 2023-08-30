#!/usr/bin/env python3
"""
A coroutine that takes no arguments
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields 10 random numbers between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
