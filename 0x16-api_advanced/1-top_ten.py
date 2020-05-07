#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress
"""
import requests


def top_ten(subreddit):
    """ function that returnthe
    titles of the first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'X-Modhash'}
    params = {'limit': 10}
    response = requests.get(
        url, headers=headers,
        allow_redirects=False, params=params
    )
    all_data = response.json()
    data = all_data.get('data')
    if data:
        hot_post = data.get('children')
        titles = [post.get('data').get('title') for post in hot_post]
        print("\n".join(titles))
    print(None)
