#!/usr/bin/python3
"""Script that fetches info about a given employee using an API
and exports it in CSV format.
"""
import csv
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


def export_to_csv(user_id, user_name, tasks):
    """Export tasks data to a CSV file."""
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='', encoding='UTF8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow(
                    [user_id, user_name, task.get('completed'),
                        task.get('title')]
                                )


def main(user_id):
    """Main function to fetch data and export to CSV."""
    # Fetch user info
    user_url = f'{BASE_URL}/users/{user_id}'
    user_data = fetch_data(user_url)
    if not user_data:
        print(f"User with ID {user_id} not found.")
        sys.exit(1)

    user_name = user_data.get('username')

    # Fetch user's TODO tasks
    tasks_url = f'{BASE_URL}/todos?userId={user_id}'
    tasks_data = fetch_data(tasks_url)

    # Export data to CSV
    export_to_csv(user_id, user_name, tasks_data)
    print(f"Data exported to {user_id}.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    if not user_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    main(int(user_id))
