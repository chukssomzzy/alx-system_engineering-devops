#!/usr/bin/python3
"""Recursively page throw the top post in a reddit"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively list a hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    params = {"count": len(hot_list), "after": after}
    headers = {"User-Agent": "chukssomzzy-app/v0.0.1"}
    r = requests.get(url, params=params, headers=headers,
                     allow_redirects=False)
    if r.status_code == 200:
        after = r.json()["data"]["after"]
        top_post_data = r.json()["data"]["children"]
        hot_list.extend(top_post_data)
        if after:
            recurse(subreddit, hot_list=hot_list, after=after)
        return hot_list
