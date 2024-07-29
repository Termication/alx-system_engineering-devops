#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get employee ID from command line arguments
    u_id = sys.argv[1]
    
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user data for the given employee ID
    user = requests.get(url + "users/{}".format(u_id)).json()
    
    # Extract username from user data
    username = user.get("username")
    
    # Fetch to-do list data for the given employee ID
    todos = requests.get(url + "todos", params={"userId": u_id}).json()
    
    # Open a CSV file for writing
    with open("{}.csv".format(u_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write to-do list items to CSV file
        [writer.writerow(
            [u_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
