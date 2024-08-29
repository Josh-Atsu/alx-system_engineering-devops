#!/usr/bin/python3
"""a function that queries the Reddit API and
returns the number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and returns the number of subscribers
    for a given subreddit.
    If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'user-Agent': 'my-custom-api v1.0.0 (BossJay)'
            }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    result = response.json
    print(result)
    return result['data']['subscribers']
