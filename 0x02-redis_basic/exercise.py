#!/usr/bin/env python3
''' Module for Redis basic excercise '''
import redis
import uuid
from typing import Union, Callable


class Cache:
    ''' Cache class for Redis '''
    def __init__(self):
        ''' Constructor '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store method '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float]:
        ''' Method to convert get data to desired format '''
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        ''' Method to convert bytes to string '''
        return self._redis.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        ''' Method to convert bytes to int '''
        return self._redis.get(key, lambda x: int(x))
