#!/usr/bin/env python3
"""
write strings to Redis
create a Cache class
store and instance of the Redis client as private variable
flush the instance
returns the random key
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(self, method: Callable) -> Callable:
    """
    count how many times methods of the Cache class are called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

class Cache():
    """
    class Cache
    """
    def __init__(self):
        """
        initialize and create an instance of the Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        returns redis string
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union(str, bytes, int, float]:
        """
        convert the data back to the desired format
        """
        val = self._redis.get(key)
        if fn is not None:
            val = fn(value)

        return val

    def get_str(self, key: str) -> str:
        """
        parametrize to a string
        """
        val = self._redis.get(key).decode('utf-8')
        return val

    def get_int(self, key: str) -> int:
        """
        parametrize to an integer
        """
        val = self._redis.get(key)
        try:
            int_val = int(val.decode('utf-8'))
        except Exception:
            int_val = 0
        return int_val
