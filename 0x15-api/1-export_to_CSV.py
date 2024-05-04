#!/usr/bin/python3
"""Export employee task information to a CSV file."""

import requests
import csv
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(f"{url}users/{user_id}").json()
    username = user.get('username')

    # Fetch todo information for the user
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    # File to save the data in CSV format
    with open(f"{user_id}.csv", 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write each task as a row in the CSV file
        for task in todos:
            writer.writerow([user_id, username, task['completed'], task['title']])

# This script uses the `csv` module for writing the CSV file, which handles proper formatting.
# It fetches user and todo data from JSONPlaceholder and writes each task for the user into the CSV.
# Each task's completion status and title are recorded along with the user's ID and username.
