"""
Define a function get_content_type(url) that, given a URL, sends a GET request and returns the content type of the response.

For example, get_content_type('http://google.com') should return 'text/html; charset=ISO-8859-1', while get_content_type('http://github.com') returns 'text/html; charset=utf-8'.
"""

import requests


def get_content_type(url):
    return requests.get(url).headers['Content-Type']


print(get_content_type('http://google.com'))
