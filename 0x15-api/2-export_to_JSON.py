#!/usr/bin/python3
"""Fetches and exports to-do list information for a given employee ID to a JSON file."""
import json
import requests
import sys

if __name__ == "__main__":
    # Retrieve the employee ID from command line arguments
    u_id = sys.argv[1]
    
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user details for the given employee ID
    user = requests.get(url + "users/{}".format(u_id)).json()
    
    # Extract the username from the user details
    username = user.get("username")
    
    # Fetch the to-do list for the given employee ID
    todos = requests.get(url + "todos", params={"userId": u_id}).json()
    
    # Open a JSON file to write the to-do list information
    with open("{}.json".format(u_id), "w") as jsonfile:
        json.dump(
            {
                u_id: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": username
                    } 
                    for t in todos
                ]
            }, 
            jsonfile
        )
