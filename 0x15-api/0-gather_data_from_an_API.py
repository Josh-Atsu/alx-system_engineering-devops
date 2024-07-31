#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
from sys import argv
import requests


def main():
    """
    main function
    """
    url = "https://jsonplaceholder.typicode.com/"
    try:
        if len(argv) == 2:
            int_n = int(argv[1])
        else:
            return
    except Exception as e:
        return
    response = requests.get(url + "users/{}".format(int_n)).json()
    Employer_name = response.get('name')
    param = {"userId": int_n}
    todo = requests.get(url + "todos", param).json()
    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
            Employer_name, len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task))

if __name__ == "__main__":
    main()
