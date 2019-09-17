#!/usr/bin/python3
# Api get
import json
import requests
from sys import argv



try:
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)
    user = response_user.json()
    todos = response_todos.json()

    row = []
    my_dict = {}

    filename = "{}.json".format(argv[1])
    for tasks in todos:
        aux = tasks['title']
        del(tasks['title'])
        del(tasks['userId'])
        del(tasks['id'])
        tasks['username'] = user['username']
        tasks['task'] = aux
        row.append(tasks)

    my_dict[argv[1]] = row
    with open(filename, 'w+') as json_file:
        json.dump(my_dict, json_file)

except Exception as err:
    print(err)
