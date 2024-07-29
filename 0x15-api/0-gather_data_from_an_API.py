#!/usr/bin/python3
"""Fetches and displays to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user data for the given employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    
    # Fetch to-do list data for the given employee ID
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    
    # Extract titles of completed tasks
    finished = [t.get('title') for t in todos if t.get('completed') is True]
    
    # Print summary of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(todos)))
    
    # Print each completed task title
    [print("\t {}".format(c)) for c in finished]
