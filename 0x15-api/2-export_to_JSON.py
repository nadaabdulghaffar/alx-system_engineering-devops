#!/usr/bin/python3
"""
Export API data into JSON file
"""
import json
import sys
from urllib.request import urlopen


def fetchUrlData(url):
    with urlopen(url) as response:
        body = response.read().decode('utf-8')
        data = json.loads(body)
        return data


if __name__ == '__main__':
    # Get the employee ID
    user_id = sys.argv[1]

    # Fetch username from HTTP response body
    username_url = f'https://jsonplaceholder.typicode.com/users?id={user_id}'
    username_data = fetchUrlData(username_url)
    username = username_data[0]['username']

    # Fetch all todo data for the given employee ID
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    todos_data = fetchUrlData(todos_url)

    # Create json object with data will add to the file
    json_data = {user_id: []}

    for tasks in todos_data:
        json_data[user_id].append({
            "task": tasks.get("title"),
            "completed": tasks.get("completed"),
            "username": username
        })

    # Write JSON file
    with open(f'{user_id}.json', 'w') as jsonfile:
        jsonWrite = json.dump(json_data, jsonfile)
