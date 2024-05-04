#!/usr/bin/python3
"""Export all employee tasks to a JSON file."""
import json
import requests

def fetch_data(url):
    """Helper function to fetch data from the given URL."""
    response = requests.get(url)
    return response.json()

def main():
    url = "https://jsonplaceholder.typicode.com/"
    users = fetch_data(f"{url}users")
    todos = fetch_data(f"{url}todos")
    
    user_task_dict = {}

    # Organize todos by user ID in the specified format
    for user in users:
        user_id = str(user['id'])
        user_task_dict[user_id] = [
            {
                "username": user['username'],
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user['id']
        ]
    
    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_task_dict, jsonfile, indent=4)

if __name__ == "__main__":
    main()
