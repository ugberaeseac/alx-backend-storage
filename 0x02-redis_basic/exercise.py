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
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """

        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key
