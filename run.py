import requests
import sys
import os

# URL of the file
URL = "https://raw.githubusercontent.com/rg772/cli-wp-campuspress-ready/main/plugins.dat"


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


def check_folder_exists(path):
    if not os.path.isdir(path):
        print(f"Directory {path} does not exist.")
        sys.exit()


def get_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


# Get arget folder, 
target_folder = input("Enter folder path")

# Checks
check_folder_exists(target_folder)

# Call the function and print the result
plugins_expected = load_url_into_array(URL)

# Scan folder 
folders_existing = get_directories(target_folder)

# Use sets to compare
plugins_expected = set(plugins_expected)
folders_existing = set(folders_existing)
set_diff = folders_existing - plugins_expected

print(folders_existing)