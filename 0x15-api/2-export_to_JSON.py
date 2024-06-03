#!/usr/bin/python3
"""Script that fetches info about a given employee using an API
and exports it in JSON format.
"""
import json
import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com'


def fetch_data(url):
    """Fetch data from the given URL and return the parsed JSON."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"An error occurred: {err}")
        sys.exit(1)


def export_to_json(user_id, user_name, tasks):
    """Export tasks data to a JSON file."""
    filename = f"{user_id}.json"
    data = {str(user_id): [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": user_name
    } for task in tasks]}

    with open(filename, 'w', encoding='UTF8') as jsonfile:
        json.dump(data, jsonfile)


def main(user_id):
    """Main function to fetch data and export to JSON."""
    # Fetch user info
    user_url = f'{BASE_URL}/users/{user_id}'
    user_data = fetch_data(user_url)
    if not user_data:
        print(f"User with ID {user_id} not found.")
        sys.exit(1)

    user_name = user_data.get('username')

    # Fetch user's todo tasks
    tasks_url = f'{BASE_URL}/todos?userId={user_id}'
    tasks_data = fetch_data(tasks_url)

    # Export data to JSON
    export_to_json(user_id, user_name, tasks_data)
    print(f"Data exported to {user_id}.json")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    if not user_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    main(int(user_id))
