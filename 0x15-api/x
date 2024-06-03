#!/usr/bin/python3
"""Script that fetches info about all employees using an API
and exports it in JSON format.
"""
import json
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def fetch_data(url):
    """Fetch data from the given URL and return the parsed JSON."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"An error occurred: {err}")
        return None


def export_all_to_json():
    """Fetch and export all tasks from all employees to a JSON file."""
    users_url = f'{BASE_URL}/users'
    users_data = fetch_data(users_url)
    if not users_data:
        return

    all_tasks = {}
    for user in users_data:
        user_id = user.get('id')
        user_name = user.get('username')

        tasks_url = f'{BASE_URL}/todos?userId={user_id}'
        tasks_data = fetch_data(tasks_url)
        if not tasks_data:
            continue

        all_tasks[str(user_id)] = [{
            "username": user_name,
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in tasks_data]

    filename = 'todo_all_employees.json'
    with open(filename, 'w', encoding='UTF8') as jsonfile:
        json.dump(all_tasks, jsonfile)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    export_all_to_json()
