from http_request import *

import json

def get_all_data():
    endpoint = f"employees"
    return get_request(endpoint)
# user interaction & interaction with an api
# class ActionHandler:
#      # method recevies api as a parameter & creating instance for Httprequest class to interact with api
#     def __init__(self,api_url):
#         self.http_request = HttpRequest(api_url)
#         self.output_file = "output.json"
# def get_all_users_data(self):
#         response = self.http_request.get_request()
#         self.print_response(response)
#         self.save_to_output({"action": "get_all"}, response)
    
#     def print_response(self, response):
#         print("Response:", response)

#     def save_to_output(self, request_data, response_data):
#         output = self.read_output_file()
#         output.append({"request": request_data, "response": response_data})
#         self.write_output_file(output)

#     def read_output_file(self):
#         try:
#             with open(self.output_file, "r") as f:
#                 return json.load(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return []

#     def write_output_file(self, output):
#         with open(self.output_file, "w") as f:
#             json.dump(output, f, indent=2)
