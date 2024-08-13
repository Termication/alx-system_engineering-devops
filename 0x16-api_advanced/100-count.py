#!/usr/bin/python3
"""Module to count occurrences of words in the titles of hot posts on a subreddit."""

from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def count_words(subreddit, word_list, after="", word_dic={}):
    """
    Recursively counts the occurrences of each word in `word_list` in the titles of hot posts on a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of words to count in the post titles.
        after (str): The "after" parameter for pagination. Defaults to an empty string.
        word_dic (dict): A dictionary to store word counts. Defaults to an empty dictionary.

    Returns:
        None: Prints the word counts sorted by frequency. If the subreddit is invalid or inaccessible, returns None.
    """
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    url = REDDIT + "r/{}/hot/.json".format(subreddit)
    params = {'limit': 100, 'after': after}

    r = get(url, headers=HEADERS, params=params, allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        js = r.json()
    except ValueError:
        return None

    try:
        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())
    except Exception:
        return None

    count_words(subreddit, word_list, after, word_dic)
