#!/usr/bin/python3
"""Rest API script that gathers data from an API."""
import json
import sys
import urllib.request

# The base API URLs for getting employee and todo objects
USER_API_URL = "https://jsonplaceholder.typicode.com/users/"
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos?userId="


def fetch_data(url):
    """Fetch data from the given URL and return the parsed JSON."""
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError as err:
        print(f"An error occurred: {err}")
        sys.exit(1)
    except json.JSONDecodeError as err:
        print(f"Error decoding JSON: {err}")
        sys.exit(1)


def get_employee_todo_progress(employee_id):
    """Get and display the TODO list progress of an employee."""
    user_url = f"{USER_API_URL}{employee_id}"
    todos_url = f"{TODO_API_URL}{employee_id}"

    # Fetch user and todos data
    employee = fetch_data(user_url)
    todos = fetch_data(todos_url)

    name = employee.get("name")
    if not name:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    done_tasks = [todo for todo in todos if todo.get("completed")]
    done_count = len(done_tasks)
    total_count = len(todos)

    print(f"Employee {name} is done with tasks({done_count}/{total_count}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(emp_id))
