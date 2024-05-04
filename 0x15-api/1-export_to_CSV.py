#!/usr/bin/python3
# Your Python script to export data in the CSV format.

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'
    user_url = f'{base_url}/{user_id}'
    response = requests.get(user_url)
    username = response.json().get('username')
    todos_url = f'{user_url}/todos'
    response = requests.get(todos_url)
    tasks = response.json()

    with open(f'{user_id}.csv', 'w') as file:
        for task in tasks:
            line = f'"{user_id}","{username}","{task.get("completed")}","{task.get("title")}"\n'
            file.write(line)
