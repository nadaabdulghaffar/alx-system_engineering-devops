#!/usr/bin/python3
"""
Script Returns information about Todo list progress of passed id
"""

import json
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    # Get the employee ID from the arguments
    employee_id = sys.argv[1]

    # Fetch the TODO list for the given employee ID
    url_todo = ('https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(employee_id))
    with urlopen(url_todo) as response:
        body = response.read().decode('UTF-8')
        todos = json.loads(body)

    # Fetch the user information for the given employee ID
    url_user = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(employee_id))
    with urlopen(url_user) as response_user:
        user_body = response_user.read().decode('UTF-8')
        user_data = json.loads(user_body)

    # Extract the employee's name
    employee_name = user_data['name']

    # Calculate the number of completed tasks and total tasks
    tasks_done = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)
    completed_tasks = len(tasks_done)

    # Print the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))
    for task in tasks_done:
        print(f"\t {task}")
