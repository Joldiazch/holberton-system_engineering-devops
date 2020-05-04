#!/usr/bin/python3
"""
script that, using REST API,
for a given employee ID, returns information
about his/her todo list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    task_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user_response = requests.get(user_url)
    task_response = requests.get(task_url)

    user_data = user_response.json()
    task_data_list = task_response.json()

    USERNAME = user_data.get('username')

    tasks = {id: [
        {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': USERNAME
        } for task in task_data_list
    ]}

    name_file = "{}.json".format(id)
    with open(name_file, 'w') as f:
        json.dump(tasks, f)
