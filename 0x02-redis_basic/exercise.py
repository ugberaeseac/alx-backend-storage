#!/usr/bin/python3

"""
write strings to redis
"""


import redis
import uuid
from typing import Union



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

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """
        store the data in Redis with a
        random generated key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key






