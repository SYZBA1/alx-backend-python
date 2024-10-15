#!/usr/bin/env python3
"""Measure runtime and return result"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime and return result"""
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
