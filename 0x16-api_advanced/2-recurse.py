#!/usr/bin/python3
"""
Script queries a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Retrieves a list of titles of all hot posts in the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:reddit_app:v1.0 (by /u/yourusername)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None  # If subreddit does not exist, return None.

    if response.status_code in [301, 302]:  # Check for redirects.
        return None  # If redirected, return None.

    if response.status_code != 200:
        return None  # Handling other bad responses like 400, 500 etc.

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)  # Recursive call to handle pagination.

    # Return the final list of hot post titles
    return hot_list


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(f"Found {len(result)} posts:")
            for title in result:
                print(title)
        else:
            print("No posts found or invalid subreddit.")
