
import requests
global API_URL  
# API_URL = "https://reqres.in/api"
class HttpRequest:
    #global API_URL  
    API_URL = "https://reqres.in/api"
    #api_url = "https://reqres.in/api"
    def __init__(self, api_url):
    #def __init__(self):
        self.API_URL = api_url
        requests.packages.urllib3.disable_warnings()

    def  perform_request(self, method, endpoint, data=None):
        url = f"{self.API_URL}/{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, verify=False)
            elif method == "POST":
                response = requests.post(url, json=data, verify=False)
            elif method == "PUT":
                response = requests.put(url, json=data, verify=False)
            elif method == "DELETE":
                response = requests.delete(url, verify=False)
            else:
                print("Invalid method.")
                return None
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404:
                print("User not found or server error occurred.")
            else:
                print(f"{method} request error:", e)
            return None
   
    def get_request(self, endpoint):
        api_url = f"{self.API_URL}/{endpoint}"
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

    def post_request(self, endpoint, data):
        api_url = f"{self.API_URL}/{endpoint}"
        if "name" in data and "job" in data:
            name = data["name"]
            job = data["job"]
            if not name or not job:
                print("Error: Name and job cannot be empty")
                return None
        else:
            print("Error: Name and job fields are required")
            return None
        try:
            response = requests.post(api_url, json=data, verify=False)
            response.raise_for_status()
            result = response.json()
            return result
        except requests.exceptions.RequestException as e:
            print("POST request error:", e)
            return None

    def put_request(self, endpoint, data):
        api_url = f"{self.API_URL}/{endpoint}"
        if "name" in data and "job" in data:
            name = data["name"]
            job = data["job"]
            if not name or not job:
                print("Error: Name and job cannot be empty")
                return None
        else:
            print("Error: Name and job fields are required")
            return None
        try:
            response = requests.put(api_url, json=data, verify=False)
            response.raise_for_status()
            result = response.json()
            return result
        except requests.exceptions.RequestException as e:
            print("PUT request error:", e)
            return None

    def delete_request(self, endpoint):
        api_url = f"{self.API_URL}/{endpoint}"
        try:
            response = requests.delete(api_url, verify=False)
            status_code = response.status_code
            response.raise_for_status()
            print(f"Delete Request Successful. Status Code: {status_code}")        
        except requests.exceptions.RequestException as e:
            print("DELETE request error:", e)
            return None
 