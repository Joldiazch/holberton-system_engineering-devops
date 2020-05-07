#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress
"""
import requests


def number_of_subscribers(subreddit):
    """ function that return number
    of subsribers to subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'X-Modhash'}
    response = requests.get(url, headers=headers)
    all_data = response.json()
    data = all_data.get('data')
    if data:
        subscribers = data.get('subscribers')
        if subscribers:
            return subscribers
    return 0
