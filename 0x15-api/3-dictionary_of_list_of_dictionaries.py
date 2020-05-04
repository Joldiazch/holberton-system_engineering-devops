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
    user_url = "https://jsonplaceholder.typicode.com/users/"

    user_response = requests.get(user_url)
    user_data_list = user_response.json()

    data_out = {}
    for user in user_data_list:
        USER_ID = str(user.get('id'))

        task_url = "https://jsonplaceholder.typicode.com/users/{}/todos"
        task_response = requests.get(task_url.format(user.get('id')))
        task_data_list = task_response.json()

        data_out[USER_ID] = [{
            'username': user.get('username'),
            'task': task.get('title'),
            'completed': task.get('completed'),
            } for task in task_data_list]

    name_file = "todo_all_employees.json"
    with open(name_file, 'w') as f:
        json.dump(data_out, f)
