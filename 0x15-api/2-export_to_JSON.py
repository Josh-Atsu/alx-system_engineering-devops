#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()

    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params)
    todos = todos_response.json()

    data_to_export = {user_id: []}
    for t in todos:
        task_details = {"task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username")}
        data_to_export[user_id].append(task_details)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile)
