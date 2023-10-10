#!/usr/bin/python3
"""Recursively page throw the top post in a reddit"""


import requests
import re
from operator import itemgetter


def count_words(subreddit, word_list, after=None):
    """Recursively list a hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}
    headers = {"User-Agent": "chukssomzzy-app/v0.0.1"}
    r = requests.get(url, params=params, headers=headers,
                     allow_redirects=False)
    if type(word_list) == list:
        word_list_copy = {}
        for word in word_list:
            word_list_copy[word.lower()] = 0
        word_list = word_list_copy
    if r.status_code == 200:
        after = r.json()["data"]["after"]
        hot_articles = r.json()["data"]["children"]
        for article in hot_articles:
            article_title = article["data"]["title"].lower()
            for word in word_list:
                p = re.compile(r'{}[^\.!\w]?'.format(word))
                word_list[word] += len(p.findall(article_title))
        if after:
            count_words(subreddit, word_list, after)
        else:
            for word, val in sorted(word_list.items(),
                                    key=itemgetter(1),
                                    reverse=True):
                if val != 0:
                    print(f"{word.strip()}: {val}")
