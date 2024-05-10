#!/usr/bin/python3
"""
Script queries a list of aaaalll hot posts on a given Reddit subr.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    
    """ retrieves a list of titles of all hot postsin subr""".

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:MahlaMed"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the final list of hot post titles
    return hot_list
