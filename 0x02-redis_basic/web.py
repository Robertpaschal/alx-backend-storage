#!/usr/bin/env python3
"""
This module provides a function to fetch web pages,
count accesses, and cache the result.
"""

import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a URL is accessed.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        key = f"count:{url}"
        redis_client.incr(key)
        return method(url, *args, **kwargs)
    return wrapper


def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the result of a URL fetch for 10 seconds.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        cache_key = f"cache:{url}"
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')

        result = method(url, *args, **kwargs)
        redis_client.setex(cache_key, 10, result)
        return result
    return wrapper


@count_calls
@cache_page
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a given URL and return it.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
