#!/usr/bin/python3
"""For a given employee ID, returns information about his/her TODO list
progress"""
from sys import argv
import json
import requests

if __name__ == '__main__':
    try:
        id = int(argv[1])
        url_user_task = \
            f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        url_user = f'https://jsonplaceholder.typicode.com/users/{id}'
        r_task = requests.get(url_user_task)
        r_user = requests.get(url_user)
        employee_tasks = r_task.json()
        employee_username = r_user.json().get('username')
        with open(f'{id}.json', 'w', encoding='utf-8') as f:
            task_arr = []
            employee_task_info = {}
            for task in employee_tasks:
                task_info = {}
                task_info['task'] = task.get('title')
                task_info['completed'] = task.get('completed')
                task_info['username'] = employee_username
                task_arr.append(task_info)
            employee_task_info[f'{id}'] = task_arr
            json.dump(employee_task_info, f)

    except Exception as e:
        print(e)
        exit(1)
    else:
        exit(0)
