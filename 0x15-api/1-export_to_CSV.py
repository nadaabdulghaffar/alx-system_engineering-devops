#!/usr/bin/python3
"""
Export API data into CSV file
"""
import csv
import json
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    # Get the employee ID
    user_id = sys.argv[1]

    # Extract username from HTTP response body
    username_url = f'https://jsonplaceholder.typicode.com/users?id={user_id}'
    with urlopen(username_url) as usrname_response:
        username_body = usrname_response.read().decode('utf-8')
        userdata = json.loads(username_body)
        username = userdata[0]['username']

    # Fetch all todos data for the given employee ID
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    with urlopen(todos_url) as todos_response:
        todos_body = todos_response.read().decode('utf-8')
        todos_data = json.loads(todos_body)

    # Write CSV file
    with open(f'{user_id}.csv', "w") as csvfile:
        csvWriter = csv.writer(
            csvfile, quoting=csv.QUOTE_ALL, lineterminator='\n'
            )

        for tasks in todos_data:
            csvWriter.writerow(
                [user_id, username, tasks.get("completed"), tasks.get("title")]
                )
