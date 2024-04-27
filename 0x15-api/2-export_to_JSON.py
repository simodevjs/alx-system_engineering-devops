#!/usr/bin/python3
# Using what you did in the task #0, extend your Python
# script to export data in the JSON format.

import json
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    url = jsonplaceholder + '/' + USER_ID
    response = requests.get(url)
    username = response.json().get('username')
    todo_url = url + '/todos'
    response = requests.get(todo_url)
    tasks = response.json()
    dict = {USER_ID: []}
    for task in tasks:
        dict[USER_ID].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
        with open('{}.json'.format(USER_ID), 'w') as f:
            json.dump(dict, f)