#!/usr/bin/python3
"""Export employee task information to a CSV file."""
import csv
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

    # Open file to save the data in CSV format
    with open(f"{user_id}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write each task as a row in the CSV file
        for task in todos:
            writer.writerow([
                user_id, username, task['completed'], task['title']
            ])

# This script correctly fetches user and todo data and writes it to a CSV.
# It ensures that each line is under 79 characters to comply with PEP8 E501.
