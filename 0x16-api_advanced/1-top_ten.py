#!/usr/bin/python3
"""
Script prints hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print titles of the TEN hottest posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:MahlaMed"
    }

    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")

    [print(c.get("data").get("title")) for c in results.get("children")]
