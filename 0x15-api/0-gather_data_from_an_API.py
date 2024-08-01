#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    """
    main function
    """
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = int(sys.argv[1])

    response_user = requests.get(url + "users/{}".format(employee_id))
    response = response_user.json()

    param = {"userId": employee_id}
    todos = requests.get(url + "todos", params=param)
    todo = todos.json()

    completed = []
    for t in todo:
        if t.get("completed") is True:
            completed.append(t.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
            response.get("name"), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task))
