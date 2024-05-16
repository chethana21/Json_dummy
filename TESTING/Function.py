import requests
import json

def get_common_name_count():
    # Define the API URL
    api_url = "https://restcountries.com/v3.1/all/?fields=name,capital"
    try:
        # Make a GET request to the API
        response = requests.get(api_url,verify=False)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            names = [country['name']['common'] for country in data]
            common_name_count = len(set(names))
            return common_name_count
        else:
            print(f"API request failed with status code {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Read the JSON file
def compare_common_name_count():
    with open('output.json', 'r') as json_file:
        json_data = json.load(json_file)
        expected_count = json_data.get("Total Countries")

# Call the function to get the common name count
    common_name_count = get_common_name_count()

    if common_name_count is not None:
        print(f"Total count of common names from API: {common_name_count}")
        common_name_count = int(common_name_count)
        expected_count = int(expected_count)
        return common_name_count == expected_count
    return False

result = compare_common_name_count()
print(result)

