#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress
"""
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

    EMPLOYEE_NAME = user_data.get('name')

    completed_tasks = [
        task.get('title') for task in task_data_list if task.get('completed')
    ]

    TOTAL_NUMBER_OF_TASKS = len(task_data_list)
    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    msg = [
        "Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS),
    ]
    msg += completed_tasks
    print("\n\t ".join(msg))
