#!/usr/bin/env python3
"""
This module contains a class and an instance of a redis client
"""
import redis
import uuid
from typing import Union


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
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
