#!/usr/bin/env python3
''' Module for Redis basic excercise '''
import redis
import uuid
import functools
from typing import Union, Callable


# how to define a decorator
def count_calls(method: Callable) -> Callable:
    ''' Decorator to count the number of calls '''

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper function '''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Decorator to store the history of inputs and outputs for a function '''

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper function '''
        input_keys = method.__qualname__ + ":inputs"
        output_keys = method.__qualname__ + ":outputs"
        self._redis.rpush(input_keys, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_keys, str(output))
        return output

    return wrapper


class Cache:
    ''' Cache class for Redis '''
    def __init__(self):
        ''' Constructor '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
