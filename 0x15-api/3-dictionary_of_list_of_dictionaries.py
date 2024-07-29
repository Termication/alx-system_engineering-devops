#!/usr/bin/python3
"""Fetches and exports to-do list information of all employees to a JSON file."""
import json
import requests

if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch details of all users
    users = requests.get(url + "users").json()
    
    # Open a JSON file to write the to-do list information of all employees
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            {
                u.get("id"): [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": u.get("username")
                    } 
                    for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()
                ] 
                for u in users
            }, 
            jsonfile
        )
