#!/usr/bin/env python3

"""
write strings to redis
"""


import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps



def count_calls(method: Callable) -> Callable:
    """
    count the number of times
    methods in Cache class is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wraper function"""
        key = method.__qualname__    
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper



class Cache():
    """
    cache class for storing and
    retrieving data from Redis
    """

    def __init__(self):
        """
        initialize redis and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    @count_calls
    def store(self, data: Union[str, bytes, float, int]) -> str:
        """
        store the data in Redis with a
        random generated key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key



    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    
    def get_str(self, key: str) -> Optional[str]:
        """
        convert redis data to UTF-8 string
        """
        value = self._redis.get(key).decode('utf-8')
        return value

    def get_int(self, key: str) -> int:
        """
        convert redis data to int
        """
        value = self._redis.get(key).decode('utf-8')
        try:
            int_value = int(value)
        except Exception:
            int_value = 0
        return int_value







