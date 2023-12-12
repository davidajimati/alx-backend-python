#!/usr/bin/env python3

"""
asynchronous coroutine that takes in an integer argument (max_delay,
with a default value of 10) named wait_random that waits
for a random delay between 0and max_delay (included and float value)
seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_wait: int = 10) -> float:
    """
    wait_random accepts a variable, generates a random number,
    waits for that long and returns it
    """
    randNum = random.uniform(0, max_wait)
    await asyncio.sleep(randNum)
    return (randNum)
