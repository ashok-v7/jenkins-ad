import os

# Get the current working directory (Jenkins workspace root)
workspace_dir = os.getcwd()

# Construct the relative path to the BTKN file
file_path = os.path.join(workspace_dir, "data/workspaces/ssops/BTKN")

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
