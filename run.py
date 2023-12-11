import requests
import sys
import os

# URL of the file
URL = "https://raw.githubusercontent.com/rg772/cli-wp-campuspress-ready/main/plugins.dat"

"""
This function sends a GET request to the specified URL and returns the response text as an array of lines.

Args:
    URL (str): The URL to send the GET request to.

Returns:
    list: A list of lines in the response text, or None if the request was unsuccessful.
"""
def load_url_into_array(URL):
    # Send a GET request to the URL
    response = requests.get(URL)

    # Check if the request was successful
    if response.status_code == 200:
        arr = response.text.split('\n')
        return arr
    else:
        print(f"Failed to fetch the file. HTTP status code: {response.status_code}")
        return None

"""
This function checks if a directory exists and exits the program if it does not.

Args:
    path (str): The path of the directory to check.
"""
def check_folder_exists(path):
     if not os.path.isdir(path):
        print(f"Directory {path} does not exist.")
        sys.exit()

"""
This function scans a directory and returns all containing directories in a list.

Args:
    path (str): The path of the directory to scan.

Returns:
    list: A list of directory names in the specified path.
"""
def get_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


# Get arget folder
target_folder = sys.argv[1] 

# Checks
check_folder_exists(target_folder)

# Call the function and print the result
plugins_expected = load_url_into_array()

# Scan folder 
folders_existing = get_directories(target_folder)

