#!/usr/bin/env python3
"""
This module contains a class and an instance of a redis client
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class for storing and retrieving data from Redis.
    """
    def __init__(self) -> None:
        """
        Initialize the Cache instance, setting up a Redis client and
        flushing the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key,
        store the input data in Redis using the random key and
        return the key.
        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None) -> Union[
                str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the given key and an optional
        conversion function.
        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): A callable used to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, possibly
            converted by fn.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis using the given key.
        Args:
            key (str): The key under which the data is stored.

        Returns:
            Optional[str]: The retrieved string data, or None if not found.
        """
        return self._redis.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis using the given key.
        Args:
            key (str): The key under which the data is stored.

        Returns:
            Optional[int]: The retrieved integer data, or None if not found.
        """
        return self._redis.get(key, int)
