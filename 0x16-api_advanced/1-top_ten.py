#!/usr/bin/python3
"""Module to query the top 10 hot posts of a subreddit using the Reddit API."""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to retrieve and print the titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints 'None' if the subreddit is not found or inaccessible.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        print('None')
    else:
        for post in response.json().get("data", {}).get("children", []):
            print(post.get("data", {}).get("title", "None"))
