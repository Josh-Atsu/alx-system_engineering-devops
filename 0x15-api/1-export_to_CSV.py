#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.json
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()

    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()
    
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for t in todos:
            writer.writerow([user_id, user.get("username"),
                    t.get("completed"), t.get("title")])
