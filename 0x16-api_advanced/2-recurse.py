#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function that returnthe
    titles of the first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'X-Modhash'}
    params = {'limit': 100, 'after': after}
    response = requests.get(
        url, headers=headers,
        allow_redirects=False, params=params
    )
    all_data = response.json()
    data = all_data.get('data')
    if data:
        hot_post = data.get('children')
        hot_list += [post.get('data').get('title') for post in hot_post]
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
