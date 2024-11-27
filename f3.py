import os

def read_file_content():
    # Construct the file path relative to the current working directory
    print("getcwd",os.getcwd())
    file_path = os.path.join(os.getcwd(), "data/workspaces/ssops/BTKN")
    print("file_path-->",file_path)

    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Contents of the file {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    read_file_content()
