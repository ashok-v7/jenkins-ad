import os

# Construct the absolute path to the file
file_path = "/data/workspaces/ssops/BTKN"

try:
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Contents of the file {file_path}:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
