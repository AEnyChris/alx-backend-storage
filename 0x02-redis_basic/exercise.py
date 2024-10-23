#!/usr/bin/env python3
"""Defines the class Cache"""
from uuid import uuid4
from typing import Any
import redis


class Cache:
    """The Cache class for storing string to redis"""
    def __init__(self) -> None:
        """initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        stores data into redis with a random key (uuid4)
        and returns the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
