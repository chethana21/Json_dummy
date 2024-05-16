import requests
#from api_config import API_URL
API_URL = "https://reqres.in/api"
# Disable SSL certificate verification
requests.packages.urllib3.disable_warnings()

def get_request(endpoint):
    api_url = f"{API_URL}/{endpoint}"
    try:
        response = requests.get(api_url, verify=False)
        response.raise_for_status()
        if response.text:
            data = response.json()
            return data
        else:
            print("empty response")
            return None
    except requests.exceptions.RequestException as e:
        print("GET request error:", e)
        return None

def post_request(endpoint, data):
    api_url = f"{API_URL}/{endpoint}"
    if data is None or not any(data.values()):
        print("Error: Empty data")
        return None
    try:
        response = requests.post(api_url, json=data, verify=False)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print("POST request error:", e)
        return None

def put_request(endpoint, data):
    api_url = f"{API_URL}/{endpoint}"
    try:
        response = requests.put(api_url, json=data, verify=False)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print("PUT request error:", e)
        return None

def delete_request(endpoint):
    api_url = f"{API_URL}/{endpoint}"
    try:
        response = requests.delete(api_url, verify=False)
        status_code = response.status_code
        response.raise_for_status()
        print(f"Delete Request Successful. Status Code: {status_code}")        
    except requests.exceptions.RequestException as e:
        print("DELETE request error:", e)
        return None