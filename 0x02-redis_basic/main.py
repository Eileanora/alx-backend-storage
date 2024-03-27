#!/usr/bin/env python3
"""
Main file
"""
import redis

from web import get_page
url = 'http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.co.uk'
print(get_page(url))
print(get_page(url))
print(get_page(url))
print(get_page(url))

