
import json
import requests
from http_request import HttpRequest
class UserManager:
    OUTPUT_FILE = "output.json"
    def __init__(self, api_url):
        self.http_request = HttpRequest(api_url)
        #self.API_URL = API_URL
        
   
    def read_output_file(self):
        try:
            with open(UserManager.OUTPUT_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    
    def write_output_file(self,output):
        with open(UserManager.OUTPUT_FILE, "w") as f:
            json.dump(output, f, indent=2)

    def get_user_data(self,user_id):
        user_id = input("Please enter the user ID: ")
        endpoint = f"users/{user_id}"
        #return HttpRequest.get_request(endpoint)
        return self.http_request.perform_request("GET",endpoint)
    
    def get_all_users_data(self):
            endpoint = "users"
            return HttpRequest.get_request(endpoint)
            #return self.http_request.perform_request("GET",endpoint)
    def create_user(self,endpoint,data):
            name = input("Please enter the user's name: ")
            job = input("Please enter the user's job: ")
            self.endpoint = "users"
            #return HttpRequest.post_request(endpoint, {"name": name, "job": job})
            self.data = {"name": name, "job": job}
            return self.http_request.perform_request("POST",endpoint,data)
    def update_user():
        user_id = input("Please enter the user ID to update: ")
        endpoint = f"users/{user_id}"
        data = {"name": input("Enter the new name: "), "job": input("Enter the new job: ")}
        return HttpRequest.put_request(endpoint, data)

    def delete_user():
        user_id = input("Please enter the user ID to delete: ")
        endpoint = f"users/{user_id}"
        return HttpRequest.delete_request(endpoint)

    def perform_action(self,action):
        output =self.read_output_file()
        if action == "get_all":
            response = self.http_request.get_request("GET", "users")
        elif action == "get":
            user_id = input("Please enter the user ID: ")
            response = self.http_request.get_request("GET", f"users/{user_id}")
        elif action == "create":
            name = input("Please enter the user's name: ")
            job = input("Please enter the user's job: ")
            response = self.http_request.post_request("POST", "users", {"name": name, "job": job})
        elif action == "update":
            user_id = input("Please enter the user ID to update: ")
            data = {"name": input("Enter the new name: "), "job": input("Enter the new job: ")}
            response = self.http_request.put_request("PUT", f"users/{user_id}", data)
        elif action == "delete":
            user_id = input("Please enter the user ID to delete: ")
            response = self.http_request.delete_request("DELETE", f"users/{user_id}")
        else:
            print("Invalid action")
            return

        response_info = {
            "action": action,
            "response": response
        }

        output.append(response_info)
        self.write_output_file(output)
        print("Response:", response)