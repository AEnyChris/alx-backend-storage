#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis = redis.Redis()



def url_tracker(method: Callable) -> Callable:
    """
    Decorator to track get request on a url.
    Counts requests and content is cached for 10 seconds
    """
    @wraps(method)
    def trigger(url) -> str:
        '''The wrapper function.
        '''
        redis.incr(f'count:{url}')
        response = redis.get(f'response:{url}')
        if response:
            return response.decode('utf-8')
        response = method(url)
        redis.set(f'count:{url}', 0)
        redis.setex(f'response:{url}', 10, response)
        return response
    return trigger


@url_tracker
def get_page(url: str) -> str:
    """
    gets the content of a url, caches it and tracks how
    many times it was requested
    """
    return requests.get(url).text
