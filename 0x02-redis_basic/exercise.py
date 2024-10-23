#!/usr/bin/env python3
"""Define class Cache for data storage"""
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """the class Cache for storing 
    data in a Redis data storage.
    """
    def __init__(self) -> None:
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a value `data` in a Redis data 
        storage and returns the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
