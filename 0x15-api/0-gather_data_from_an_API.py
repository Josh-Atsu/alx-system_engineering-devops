#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    main function
    """
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(argv[1])
    response = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = response.get('name')
    param_1 = {"userId": employee_id}
    todo = requests.get(url + "todos", param_1).json()
    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task))
