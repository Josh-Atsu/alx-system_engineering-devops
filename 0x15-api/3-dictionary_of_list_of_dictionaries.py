#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":
    """main task"""
    url = "https://jsonplaceholder.typicode.com/"

    users_all = requests.get(url + "users/").json()

    data_to_export = {}
    for user in users_all:
        user_id = user["id"]

        todos_list = requests.get(url + "todos?userId={}"
                                  .format(user_id)).json()

        data_in_todo = {user_id: []}
        for todo in todos_list:
            task_info = {"username": user.get("username"),
                         "task": todo.get("title"),
                         "completed": todo.get("completed")}
            data_in_todo[user_id].append(task_info)

        data_to_export.update(data_in_todo)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile)
