import requests
# requests of API
# class HttpRequest:
#     # method recevies api as a parameter & initializes an instance with the given url
#     def __init__(self,api_url):
#         self.API_URL = api_url
#         requests.packages.urllib3.disable_warnings()

#     def perform_request(self,method, endpoint, data=None):
#         url = f"{self.API_URL}/{endpoint}"
#         try:
#             if method == "GET":
#                 response = requests.get(url, verify=False)
#             elif method == "POST":
#                 response = requests.post(url, json=data, verify=False)
#             elif method == "PUT":
#                 response = requests.put(url, json=data, verify=False)
#             elif method == "DELETE":
#                 response = requests.delete(url, verify=False)
#             else:
#                 print("Invalid method.")
#                 return None
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404:
#                 print("User not found or server error occurred.")
#             else:
#                 print(f"{method} request error:", e)
#             return None

def get_request(self):
        api_url = f"{self.API_URL}"
        try:
            response = requests.get(api_url, verify=False, timeout=10)
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

    # def post_request(self, endpoint, data):
    #     return self.perform_request("POST", endpoint, data)

    # def put_request(self, endpoint, data):
    #     return self.perform_request("PUT", endpoint, data)

    # def delete_request(self, endpoint):
    #     api_url = f"{self.API_URL}/{endpoint}"
    #     try:
    #         response = requests.delete(api_url, verify=False)
    #         status_code = response.status_code
    #         response.raise_for_status()
    #         if response.text:
    #             data = response.json()
    #             return data
    #         else:
    #             print(f"Delete Request Successful. Status Code: {status_code}")
    #             return None
    #     except requests.exceptions.RequestException as e:
    #         print("DELETE request error:", e)
    #         return None