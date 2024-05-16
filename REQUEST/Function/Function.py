
import requests
import json

requests.packages.urllib3.disable_warnings()            # Disable SSL certificate verification

def get_request(api_url):
    try:
        response = requests.get(api_url, verify=False) #disables the security certificate check and made the program error-free to execute.
        response.raise_for_status()                     # Raise an exception for unsuccessful responses9i
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("GET request error:", e)
        return None

def post_request(api_url, data):
    try:
        response = requests.post(api_url, json=data, verify=False)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print("POST request error:", e)
        return None
 
def put_request(api_url, data):
    try:
        response = requests.put(api_url, json=data, verify=False)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print("PUT request error:", e)
        return None
 
def delete_request(api_url):
    try:
        response = requests.delete(api_url, verify=False)
        status_code = response.status_code
        response.raise_for_status()
        print(f"Delete Request Successful. Status Code: {status_code}")
    except requests.exceptions.RequestException as e:
        print("DELETE request error:", e)
        return None

def main():
    api_url = input("Please enter the API URL: ")
    method = input("Please enter the HTTP method (GET, POST, PUT, DELETE): ")
    if method == "GET":
        result = get_request(api_url)
    elif method == "POST":
        data = input("Please enter the data as a JSON dictionary: ")
        try:
            data = json.loads(data)
            result = post_request(api_url, data)
        except json.JSONDecodeError:
            print("Invalid JSON data.")
            result = None
    elif method == "PUT":
        data = input("Please enter the data as a JSON dictionary for modifying: ")
        try:
            data = json.loads(data)
            result = put_request(api_url, data)
        except json.JSONDecodeError:
            print("Invalid JSON data.")
            result = None
    elif method == "DELETE":
        key_to_data = int(input("Please enter the data to be Deleted from JSON dictionary: "))
        del_url = f'{api_url}/{key_to_data}'
        delete_request(del_url)
        result = None
    else:
        print("Invalid method.")
        result = None
    if result is not None:
        print("Response:", result)
if __name__ == "__main__":
    main()
