#!/usr/bin/python3
"""
A function that queries the Reddit API
and returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
    It returns the number of total subscribers
    Args:
        subreddit (str): The name of the subreddit to query.
    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
