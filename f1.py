
import requests
import json
from datetime import datetime


def fetch_data():
    # URL of the public API
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Fetch data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON data
        data = response.json()

        # Write data to a file with a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"api_data_{timestamp}.json"

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Data successfully fetched and saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_data()

