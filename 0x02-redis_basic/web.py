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
        key = f'count:{url}'
        redis_client.incr(key)
        result = redis_client.get(key)
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_client.set(key, 0)
        redis_client.setex(key, 10, result)
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
