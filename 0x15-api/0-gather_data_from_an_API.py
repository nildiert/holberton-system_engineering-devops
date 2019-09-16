#!/usr/bin/python3
# Api get
import requests
from sys import argv

try:
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)
    user = response_user.json()
    todos = response_todos.json()

    completed = 0
    tasks = []
    for task in todos:
        if task['completed'] is True:
            completed += 1
            tasks.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], completed, len(todos)))
    for title_task in tasks:
        print("\t{}".format(title_task))

except Exception as err:
    pass
