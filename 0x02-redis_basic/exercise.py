#!/usr/bin/env python3
"""Defines the class Cache"""
from uuid import uuid4
from typing import Union
import redis


class Cache:
    """The Cache class for storing data to redis"""
    def __init__(self) -> None:
        """initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        stores data into redis with a random key (uuid4)
        and returns the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
