#!/usr/bin/python3
"""For a given employee ID, returns information about his/her TODO list
progress"""

from sys import argv
import csv
import requests

if __name__ == "__main__":
    try:
        id = int(argv[1])
        url_user_task = \
            f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        url_user = \
            f'https://jsonplaceholder.typicode.com/users/{id}'
        r_task = requests.get(url_user_task)
        r_user = requests.get(url_user)
        employee_tasks = r_task.json()
        employee_username = r_user.json().get('username')
        with open(f'{id}.csv', 'w', newline='') as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            for task in employee_tasks:
                taskwriter.writerow(
                    [id, employee_username, task.get("completed"),
                     task.get("title")])
    except Exception as e:
        print(e)
        exit(1)
    else:
        exit(0)
