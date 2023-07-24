#!/usr/bin/python3
"""Todos for employee in dict"""
import json

import requests

if __name__ == "__main__":
    employees_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    employees = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()

    employees_username = {}
    for employee in employees:
        employees_username[employee.get('id')] = employee.get('username')
    employees_todos_edit = {}
    for employee_todo in employees_todos:
        employee_todo_dict = {}
        employee_id = employee_todo.get('userId')
        employee_todo_dict['username'] = employees_username.get(
            employee_id)
        employee_todo_dict['task'] = employee_todo.get('title')
        employee_todo_dict['completed'] = employee_todo.get('completed')
        if employees_todos_edit.get(employee_id):
            employees_todos_edit[employee_id].append(employee_todo_dict)
        else:
            employees_todos_edit[employee_id] = [employee_todo_dict]
    with open('todo_all_employees.json', 'w', encoding='utf8') as f:
        json.dump(employees_todos_edit, f)
