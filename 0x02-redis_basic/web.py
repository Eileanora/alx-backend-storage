''' Module for Redis basic excercise '''
import redis
from typing import Callable
import functools
import requests

redis_db = redis.Redis()


def cache_url(method: Callable) -> Callable:
    ''' Decorator to store the history of inputs and outputs for a function\
        and caches the result of the URL for 10 sec '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper function '''
        url = args[0]
        key = "count:" + url
        redis_db.incr(key)
        cached = redis_db.get("result:" + url)
        if cached:
            return cached.decode('utf-8')
        cached = method(url)
        redis_db.setex("result:" + url, 10, cached)
        return cached

    return wrapper


@cache_url
def get_page(url: str) -> str:
    ''' Get the HTML content of a particular URL and return it '''
    return requests.get(url).text
