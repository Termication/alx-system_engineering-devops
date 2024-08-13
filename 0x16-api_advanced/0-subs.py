#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or inaccessible.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}  # Set a custom User-Agent to avoid request errors
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Successfully retrieved the data, extract number of subscribers
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        # Return 0 if the subreddit is invalid or inaccessible
        return 0
