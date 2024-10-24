#!/usr/bin/env python3
"""Define class Cache for data storage"""
from uuid import uuid4
from functools import wraps
import redis
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    """counts how many times a method of Cache class is called"""
    @wraps(method)
    def trigger(self, *args, **kwargs) -> Any:
        """invokes the given method after increment of counter"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return trigger


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and output for a function"""
    @wraps(method)
    def trigger(self, *args, **kwargs) -> Any:
        """
        adds the input and output of method
        to a list and returns the output
        """
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output
    return trigger


class Cache:
    """the class Cache for storing
    data in a Redis data storage.
    """
    def __init__(self) -> None:
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
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
