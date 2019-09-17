#!/usr/bin/python3
# Api get
import json
import requests


try:
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)
    user = response_user.json()
    todos = response_todos.json()

    row = []
    person = {}
    my_dict = {}

    for user_dict in user:
        for todo in todos:
            if todo['userId'] == user_dict['id']:
                person['username'] = user_dict.get('username')
                person['task'] = todo.get('title')
                person['completed'] = todo.get('completed')
                row.append(person)
                person = {}
        my_dict[user_dict['id']] = row
        row = []

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(my_dict, json_file)


except Exception as err:
    pass
