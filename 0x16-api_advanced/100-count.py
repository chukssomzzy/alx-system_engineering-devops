#!/usr/bin/python3
"""Recursively page throw the top post in a reddit"""


import requests


def count_words(subreddit, word_list, after=None):
    """Recursively list a hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}
    headers = {"User-Agent": "chukssomzzy-app/v0.0.1"}
    r = requests.get(url, params=params, headers=headers,
                     allow_redirects=False)
    if type(word_list) == str:
        word_list_copy = {}
        for word in word_list:
            word_list_copy[word] = 0
        word_list = word_list_copy
    if r.status_code == 200:
        after = r.json()["data"]["after"]
        hot_articles = r.json()["data"]["children"]
        for article in hot_articles:
            for word in word_list:
                while article.find(word) > -1:
                    article = article[article.find(word):]
                    word_list[word] += 1
        for word, val in word_list.items():
            print(f"{word}: {val}")
