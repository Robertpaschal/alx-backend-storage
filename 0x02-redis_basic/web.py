#!/usr/bin/env python3
"""
This module provides a function to fetch web pages,
count accesses, and cache the result.
"""
import requests
import redis
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        redis_client.incr(f'count:{url}')
        result = redis_client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_client.set(f'count:{url}', 0)
        redis_client.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a given URL and return it.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL
    """
    response = requests.get(url)
    return response.text
