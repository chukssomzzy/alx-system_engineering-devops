#!/usr/bin/python3
"""For a given employee ID, returns information about his/her TODO list
progress"""

from sys import argv
import requests

if __name__ == "__main__":
    try:
        id = int(argv[1])
        url_user_task = \
            f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        url_user = f'https://jsonplaceholder.typicode.com/users/{id}'
        r_task = requests.get(url_user_task)
        r_user = requests.get(url_user)
        employee_tasks = r_task.json()
        employee_name = r_user.json().get('name')
        task_comp = 0
        total_task = 0
        completed_task_title = []
        for task in employee_tasks:
            total_task += 1
            if task.get('completed'):
                task_comp += 1
                completed_task_title.append(task.get('title'))
        print(
            f"Employee {employee_name} \
is done with tasks({task_comp}/{total_task}):")

        for task_title in completed_task_title:
            print(f"\t {task_title}")
    except Exception as e:
        print(e)
        exit(1)
    else:
        exit(0)
