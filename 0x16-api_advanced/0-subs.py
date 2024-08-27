#!/use/bin/python3
"""a function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and returns the number of subscribers
    for a given subreddit.
    If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'user-Agent': 'Linux:0x16-Advanced API:v1.0.0 (BossJay)'
            }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
