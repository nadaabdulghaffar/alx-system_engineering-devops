#!/usr/bin/python3
"""
scprit that Records all tasks from all employees
"""
import json
from urllib.request import urlopen


def FetchUrlData(url):
    with urlopen(url) as response:
        body = response.read().decode('utf-8')
        data = json.loads(body)
        return data


if __name__ == "__main__":

    # Get all employees personal data
    users_url = f'https://jsonplaceholder.typicode.com/users'
    users_data = FetchUrlData(users_url)

    # Get all todo data for the given employee
    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    todos_data = FetchUrlData(todos_url)

    # Create dictionary of list of dictionaries has employee data
    dict_data = {user.get('id'): [] for user in users_data}

    for task in todos_data:
        userid = task.get('userId')
        username = users_data[userid - 1].get('username')
        dict_data[task.get('userId')].append({
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        })
    # Write JSON file
    with open("todo_all_employees.json", 'w') as jsonfile:
        jsonWrite = json.dump(dict_data, jsonfile)
