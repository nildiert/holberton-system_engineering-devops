#!/usr/bin/python3
# Api get
import requests
from sys import argv
import csv


try:
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)
    user = response_user.json()
    todos = response_todos.json()

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)
    row = []
    keys = ['userId', 'username', 'completed', 'title']
    filename = "{}.csv".format(argv[1])
    for tasks in todos:
        tasks['username'] = user['username']
        for key in keys:
            row.append(tasks[key])
        try:
            with open(filename, 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
        except:
            pass
        with open(filename, 'a') as writeFile:
            writer = csv.writer(writeFile, dialect='myDialect')
            writer.writerow(row)

        row = []
    readFile.close()
    writeFile.close()


except Exception as err:
    pass
