#!/usr/bin/python3
"""Generate a Todo list for a given employee id"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]

    user = requests.get(url + f"users/{id}").json()
    todos = requests.get(url + f"todos", params={"userId": id}).json()

    tasks = [i["title"] for i in todos if i["completed"]]
    print(f"Employee {user.get('name')} is done with ", end="")
    print(f"tasks({len(tasks)}/{len(todos)}):")
    [print(f"\t {i}") for i in tasks]
