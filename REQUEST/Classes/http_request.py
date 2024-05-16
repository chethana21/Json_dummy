import requests
# requests of API
class HttpRequest:
    # method recevies api as a parameter & initializes an instance with the given url
    def __init__(self,api_url):
        self.API_URL = api_url
        requests.packages.urllib3.disable_warnings()

    def get_request(self,api_url):
        #api_url = f"{self.API_URL}/{endpoint}"
        try:
            response = requests.get(api_url, verify=False)
            status_code = response.status_code
            response.raise_for_status()
            if response.text:
                data = response.json()
                return data
            else:
                print(f"Empty Response. Status Code: {status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print("GET request error:", e)
            return None

    def post_request(self, api_url, data):
        #api_url = f"{self.API_URL}/{endpoint}"
        try:
            response = requests.post(api_url, json=data, verify=False)
            status_code = response.status_code
            response.raise_for_status()
            if response.text:
                data = response.json()
                return data
            else:
                print(f"Empty Response. Status Code: {status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print("GET request error:", e)
            return None

    def put_request(self, api_url, data):
        
        try:
            response = requests.put(api_url, json=data, verify=False)
            status_code = response.status_code
            response.raise_for_status()
            if response.text:
                data = response.json()
                return data
            else:
                print(f"Empty Response. Status Code: {status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print("GET request error:", e)
            return None

    def delete_request(self, api_url):
        #api_url = f"{self.API_URL}/{endpoint}"
        try:
            response = requests.delete(api_url, verify=False)
            status_code = response.status_code
            response.raise_for_status()
            if response.text:
                data = response.json()
                return data
            else:
                #print(f"Delete Request Successful. Status Code: {status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print("DELETE request error:", e)
            return None