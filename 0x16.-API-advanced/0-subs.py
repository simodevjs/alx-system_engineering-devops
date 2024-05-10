#!/usr/bin/python3
"""
Script queries subscribers on a given Reddit sub
"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subs on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        dict = response.json()
        subu = dict['data']['subscribers']
        return subu
    else:
        return 0
