#!/usr/bin/env python3
"""Define class Cache for data storage"""
from uuid import uuid4
import redis
from typing import Union, Callable


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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """
        retrieves and convert data from
        redis to desired format using a callable fn
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """parametarize data to string from a redis storage"""
        res = self.get(key, lambda x: x.decode('utf-8'))
        return res

    def get_int(self, key: str) -> int:
        """parametarize data to integer from a redis storage"""
        res = self.get(key, lambda x: int(x))
        return res
