import requests
API_URL = "https://jsonplaceholder.typicode.com"
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
        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404: 
            print("User not found or server error occurred.")
        else:
            print("GET request error:", e)
        return None