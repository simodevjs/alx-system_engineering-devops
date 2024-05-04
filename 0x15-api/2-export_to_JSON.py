#!/usr/bin/python3
"""Export employee task information to a JSON file."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(f"{url}users/{user_id}")
    user = user_response.json()
    username = user.get('username')

    # Fetch todo information for the user
    todos_response = requests.get(f"{url}todos", params={"userId": user_id})
    todos = todos_response.json()

    # Prepare data in the required format
    tasks_list = []
    for task in todos:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        tasks_list.append(task_info)

    # Organize data by user ID in a dictionary
    tasks_dict = {user_id: tasks_list}

    # Write the data to a JSON file
    with open(f"{user_id}.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile, indent=4)

# This script fetches data and formats it according to the given structure.
# It saves the output in a JSON file named with the user's ID.
