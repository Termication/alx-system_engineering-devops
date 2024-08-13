#!/usr/bin/python3
"""Module to recursively query and return all hot posts from a subreddit using the Reddit API."""

import requests

def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Recursively queries the Reddit API to retrieve all hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): Accumulator list to store the titles of hot posts.
        count (int): The number of posts retrieved so far.
        after (str): The "after" parameter for pagination.

    Returns:
        list: A list of titles of all hot posts, or None if the subreddit is invalid or inaccessible.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code >= 400:
        return None

    data = response.json().get("data", {})
    hot_list += [child.get("data", {}).get("title") for child in data.get("children", [])]

    if data.get("after") is None:
        return hot_list

    return recurse(subreddit, hot_list, data.get("count", count), data.get("after"))
