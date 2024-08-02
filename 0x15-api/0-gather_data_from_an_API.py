#!/usr/bin/python3
"Script Returns information about Todo list progress of passed id"

import sys
import json
from urllib.request import urlopen

if __name__ == "__main__":
    args = sys.argv[1]

    url_todo = ('https://jsonplaceholder.typicode.com/todos/?userId={}'
               .format(args))
    with urlopen(url_todo) as response:
        body = response.read().decode('UTF-8')
        data = json.loads(body)

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(args)
    with urlopen(url_user) as response_user:
        user_body = response_user.read().decode('UTF-8')
        user_data = json.loads(user_body)

    tasksDone = []
    tasksTotal = len(data)
    employeeName = user_data['name']

    for i in data:
        if i['completed'] is True:
            tasksDone.append(i['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(tasksDone), tasksTotal))
    for i in tasksDone:
        print("      {}".format(i))
