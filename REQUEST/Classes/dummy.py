# from http_request import HttpRequest
# import json

 

# class ActionHandler:
#     def __init__(self):
#         self.http_request = HttpRequest()
#         self.output_file = "output.json"

 

#     def perform_action(self, action):
#         if action == "1":
#             self.get_all_users_data()
#         elif action == "2":
#             self.get_user_data()
#         elif action == "3":
#             self.create_user()
#         elif action == "4":
#             self.update_user()
#         elif action == "5":
#             self.delete_user()
#         else:
#             print("Invalid option. Please choose again.")

 

#     def get_user_data(self):
#         user_id = input("Please enter the user ID: ")
#         response = self.http_request.get_request(f"users/{user_id}")
#         self.print_response(response)

 

#     def get_all_users_data(self):
#         response = self.http_request.get_request("users")
#         self.print_response(response)

 

#     def create_user(self):
#         name = input("Please enter the user's name: ")
#         job = input("Please enter the user's job: ")

 

#         if not name.strip() or not job.strip():
#             print("Error: Name and job cannot be empty")
#             return

 

#         data = {"name": name, "job": job}
#         response = self.http_request.post_request("users", data)
#         self.print_response(response)
#         self.save_to_output(data, response)

 

#     def update_user(self):
#         user_id = input("Please enter the user ID to update: ")
#         name = input("Enter the new name: ")
#         job = input("Enter the new job: ")

 

#         if not name.strip() or not job.strip():
#             print("Error: Name and job cannot be empty")
#             return

 

#         data = {"name": name, "job": job}
#         response = self.http_request.put_request(f"users/{user_id}", data)
#         self.print_response(response)
#         self.save_to_output(data, response)

 

#     def delete_user(self):
#         user_id = input("Please enter the user ID to delete: ")
#         response = self.http_request.delete_request(f"users/{user_id}")
#         self.print_response(response)

 

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









# ##################################################################################

# from http_request import HttpRequest
# import json
# # user interaction & interaction with an api
# class ActionHandler:
#      # method recevies api as a parameter & creating instance for Httprequest class to interact with api
#     def __init__(self,api_url):
#         self.http_request = HttpRequest(api_url)
#         self.output_file = "output.json"

#     # def perform_action(self, action):
#     #     if action == "1":
#     #         self.get_all_users_data()
#     #     elif action == "2":
#     #         self.get_user_data()
#     #     elif action == "3":
#     #         self.create_user()
#     #     elif action == "4":
#     #         self.update_user()
#     #     elif action == "5":
#     #         self.delete_user()
#     #     elif action == "6":
#     #         self.check_email()
#     #     else:
#     #         print("Invalid option. Please choose again.")

#     def get_user_data(self):
#         user_id = input("Please enter the user ID: ")
#         response = self.http_request.get_request(f"users/{user_id}")
#         self.print_response(response)
#         self.save_to_output({"user_id" : user_id}, response)

#     def get_all_users_data(self):
#         response = self.http_request.get_request("users")
#         self.print_response(response)
#         self.save_to_output({"action": "get_all"}, response)
 
#     def create_user(self):
#         name = input("Please enter the user's name: ")
#         job = input("Please enter the user's job: ")
#         if not name.strip() or not job.strip():
#             print("Error: Name and job cannot be empty")
#             return
#         data = {"name": name, "job": job}
#         response = self.http_request.post_request("users", data)
#         self.print_response(response)
#         self.save_to_output(data, response)

#     def update_user(self):
#         user_id = input("Please enter the user ID to update: ")
#         name = input("Enter the new name: ")
#         job = input("Enter the new job: ")
#         if not name.strip() or not job.strip():
#             print("Error: Name and job cannot be empty")
#             return
#         data = {"name": name, "job": job}
#         response = self.http_request.put_request(f"users/{user_id}", data)
#         self.print_response(response)
#         self.save_to_output(data, response)

#     def delete_user(self):
#         user_id = input("Please enter the user ID to delete: ")
#         response = self.http_request.delete_request(f"users/{user_id}")
#         self.print_response(response)

#     def check_email(self):
#         email_to_check = input("Please enter an email address to check: ")
#         all_users = self.http_request.get_request("users")  # fetching all users
#         matching_users = []

#         if all_users and "data" in all_users:
#             for user in all_users["data"]:
#                 if user.get("email") == email_to_check:
#                     matching_users.append({
#                     "id": user["id"],
#                     "first_name": user["first_name"],
#                     "last_name": user["last_name"]
#                 })

#         if matching_users:
#             print("Matching Users:")
#             for user in matching_users:
#                 print(f"ID: {user['id']}, First Name: {user['first_name']}, Last Name: {user['last_name']}")
#             with open(self.output_file,"a") as f:
#                 json.dump(matching_users, f , indent=2)
            
#         else:
#             print("No users found with the provided email address.")

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


from http_request import HttpRequest

import json

# user interaction & interaction with an api

class ActionHandler:

     # method recevies api as a parameter & creating instance for Httprequest class to interact with api

    def __init__(self,api_url):

        self.http_request = HttpRequest(api_url)

        self.output_file = "output.json"

 

    def get_user_data(self,user_id):

        response = self.http_request.get_request(f"users/{user_id}")

        self.print_response(response)

        self.save_to_output({"user_id" : user_id}, response)

 

    def get_all_user_data(self):

        page =1

        total_pages = 0

        all_user_data = []

        while True:

            response = self.http_request.get_request(f"users?page={page}")

            if "data" not in response or not response["data"]:

                break

            if total_pages == 0:

                total_pages = response["total_pages"]

            print(f"Page {page}: ")

            for user in response["data"]:

                all_user_data.append(user)

                #self.print_response(user)

                self.save_to_output({"action": "get_all_pages"},response)

            if page >= total_pages:

                break

            page +=1

        return all_user_data

    def process_all_user_data(self):

        all_user_data = self.get_all_user_data()

        for user in all_user_data:

            print(f"userId': user['id'], 'name':{user['first_name']}{user['last_name']}")

 

    def get_first_page_users_data(self):

        response = self.http_request.get_request("users")

        self.print_response(response)

        self.save_to_output({"action": "get_all"}, response)

 

    def create_user(self,name,job):

        #name = input("Please enter the user's name: ")

        #job = input("Please enter the user's job: ")

        # if not name.strip() or not job.strip():

        #     print("Error: Name and job cannot be empty")

        #     return

        data = {"name": name, "job": job}

        response = self.http_request.post_request("users", data)

        self.print_response(response)

        self.save_to_output(data, response)

        user_id = response.get("id")

        return user_id

    def update_user(self,user_id,name,job):

        # user_id = input("Please enter the user ID to update: ")

        # name = input("Enter the new name: ")

        #job = input("Enter the new job: ")

        # if not name.strip() or not job.strip():

        #     print("Error: Name and job cannot be empty")

        #     return

        data = {"name": name, "job": job}

        response = self.http_request.put_request(f"users/{user_id}", data)

        self.print_response(response)

        self.save_to_output(data, response)

        updated_user_id = response.get("id")

        return updated_user_id

    def delete_user(self,user_id):

        #user_id = input("Please enter the user ID to delete: ")

        response = self.http_request.delete_request(f"users/{user_id}")

        self.print_response(response)

 

    def find_user_by_email(self,email_to_check):

        page = 1

        matching_users = []

        while True:

 

            response = self.http_request.get_request(f"users?page={page}")

            if "data" not in response or not response["data"]:

                break

            for user in response["data"]:

                if user.get("email") == email_to_check:

                    matching_users.append({

                    "id": user["id"],

                    "first_name": user["first_name"],

                    "last_name": user["last_name"]

                })

            page +=1

 

        if matching_users:

            print("Matching Users:")

            for user in matching_users:

                print(f"ID: {user['id']}, First Name: {user['first_name']}, Last Name: {user['last_name']}")

            with open(self.output_file,"a") as f:

                json.dump(matching_users, f , indent=2)

           

        else:

            print("No users found with the provided email address.")

 

    def print_response(self, response):

        print("Response:", response)

 

    def save_to_output(self, request_data, response_data):

        output = self.read_output_file()

        output.append({"request": request_data, "response": response_data})

        self.write_output_file(output)

 

    def read_output_file(self):

        try:

            with open(self.output_file, "r") as f:

                return json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):

            return []

 

    def write_output_file(self, output):

        with open(self.output_file, "w") as f:

            json.dump(output, f, indent=2)
# from http_request import HttpRequest
# import json
# # user interaction & interaction with an api
# class ActionHandler:
#      # method recevies api as a parameter & creating instance for Httprequest class to interact with api
#     def __init__(self,api_url):
#         self.http_request = HttpRequest(api_url)
#         self.output_file = "output.json"
#         self.responses = []
#     def get_user_data(self,user_id):
        
#         response = self.http_request.get_request(f"users/{user_id}")
        
#         self.responses.append({"action": "Get User ID data", "User_id": user_id, "response":response})
#         self.save_to_output({"user_id" : user_id}, response)
        
#         #self.print_response(response)
#     def get_all_user_data(self):
#         page =1
#         total_pages = 0
#         all_user_data = []
#         while True:
#             response = self.http_request.get_request(f"users?page={page}")
#             if "data" not in response or not response["data"]:
#                 break
#             if total_pages == 0:
#                 total_pages = response["total_pages"]

#             for user in response["data"]:
#                 #all_user_data.append(user)
#                 self.responses.append({"action": "get_all_pages","response":user})
#                 self.save_to_output({"action": "get_all_pages"},response)
#             if page >= total_pages:
#                 break
#             page +=1

 
#     def create_user(self,name,job):
#         #name = input("Please enter the user's name: ")
#         #job = input("Please enter the user's job: ")
#         # if not name.strip() or not job.strip():
#         #     print("Error: Name and job cannot be empty")
#         #     return
#         data = {"name": name, "job": job}
#         response = self.http_request.post_request("users", data)
#         self.responses.append({"action": "create user","request":{"name":name,"job":job},"response":response})
#         self.save_to_output(data, response)
#         user_id = response.get("id")
#         return user_id
#     def update_user(self,user_id,name,job):
#         # user_id = input("Please enter the user ID to update: ")
#         # name = input("Enter the new name: ")
#         #job = input("Enter the new job: ")
#         # if not name.strip() or not job.strip():
#         #     print("Error: Name and job cannot be empty")
#         #     return
#         data = {"name": name, "job": job}
#         response = self.http_request.put_request(f"users/{user_id}", data)
#         self.responses.append({"action": "Update user","request":{"name":name,"job":job},"response":response})
#         self.save_to_output(data, response)
#         updated_user_id = response.get("id")
#         return updated_user_id
#     def delete_user(self,user_id):
#         #user_id = input("Please enter the user ID to delete: ")
#         response = self.http_request.delete_request(f"users/{user_id}")
#         self.responses.append(response)

#     def find_user_by_email(self,email_to_check):
#         page = 1
#         total_pages = 0
#         matching_users = []
#         while True:

#             response = self.http_request.get_request(f"users?page={page}")
#             if "data" not in response or not response["data"]:
#                 break
#             if total_pages == 0:
#                 total_pages = response["total_pages"]
#             for user in response["data"]:
#                 if user.get("email") == email_to_check:
#                     matching_users.append({
#                     "id": user["id"],
#                     "first_name": user["first_name"],
#                     "last_name": user["last_name"]
#                 })
#             if page >= total_pages:
#                 break
#             page +=1

#         if matching_users:
#             # print("Matching Users:")
#             # for user in matching_users:
            
#             self.responses.append({"action" : "Check User by email",
#                     "request":{"email":email_to_check},
#                     "response":matching_users }) 
                    
                
#                 #print(f"ID: {user['id']}, First Name: {user['first_name']}, Last Name: {user['last_name']}")
#             with open(self.output_file,"a") as f:
#                 json.dump(matching_users, f , indent=2)
            
#         else:
#             print("No users found with the provided email address.")

#     def print_response(self):
#         return self.responses
#     def print_stored_response(self):
#         for item in self.responses:
#             action = item.get("action")
#             response = item.get("response")
#             print(f"Action:{action}")
#             if response:
#                 print( "Response:")
#                 print(response)
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


# import json

# from http_request import HttpRequest

 

# class ActionHandler:

#     def __init__(self, api_url):
#         self.http_request = HttpRequest(api_url)
#         self.responses = []  # Store action, request, and response data here

#     def get_user_data(self, user_id):
#         response = self.http_request.get_request(f"users/{user_id}")
#         #self.save_to_output({"action": "get_user_data", "user_id": user_id}, response)
#         self.responses.append({"action": "get_user_data", "request": {"user_id": user_id}, "response": response})

#     def get_all_user_data(self):
#         page = 1
#         total_pages = 0
#         all_user_data = []
#         while True:

#             response = self.http_request.get_request(f"users?page={page}")
#             if "data" not in response or not response["data"]:
#                 break
#             if total_pages == 0:
#                 total_pages = response["total_pages"]
#             print(f"Page {page}:")
#             for user in response["data"]:
#                 all_user_data.append(user)
#                 # Log the action, request, and response data
#                 #self.responses.append({"action": "get_all_user_data", "request": {"page": page}, "response": user})
#             if page >= total_pages:
#                 break
#             page += 1
#         return all_user_data
#     def process_all_user_data(self):

#         all_user_data = self.get_all_user_data()

#         for user in all_user_data:

#             print(f"userId': user['id'], 'name':{user['first_name']}{user['last_name']}")

#     def get_first_page_users_data(self):

#         response = self.http_request.get_request("users")

#         #self.save_to_output({"action": "get_first_page_users_data"}, response)

#         self.responses.append({"action": "get_first_page_users_data", "request": {}, "response": response})

#     def create_user(self, name, job):
#         data = {"name": name, "job": job}
#         response = self.http_request.post_request("users", data)
#        # self.save_to_output({"action": "create_user", "name": name, "job": job}, response)
#         user_id = response.get("id")
#         self.responses.append({"action": "create_user", "request": {"name": name, "job": job}, "response": user_id})
#         return user_id

#     def update_user(self, user_id, name, job):
#         data = {"name": name, "job": job}
#         response = self.http_request.put_request(f"users/{user_id}", data)
#         #self.save_to_output({"action": "update_user", "user_id": user_id, "name": name, "job": job}, response)
#         updated_user_id = response.get("id")
#         self.responses.append({"action": "update_user", "request": {"user_id": user_id, "name": name, "job": job}, "response": updated_user_id})
#         return updated_user_id

#     def delete_user(self, user_id):
#         response = self.http_request.delete_request(f"users/{user_id}")
#         #self.save_to_output({"action": "delete_user", "user_id": user_id}, response)
#         self.responses.append({"action": "delete_user", "request": {"user_id": user_id}, "response": response})

#     def find_user_by_email(self, email_to_check):
#         page = 1
#         #total_pages = None
#         matching_users = []
#         #while total_pages is None or page <= total_pages:
#         print("debuging")
#         while True:
#             response = self.http_request.get_request(f"users?page={page}")
#             # if response is None:
#             #     break
#             if "data" not in response :
#             #or not response["data"]:
#                # break
#             #if page == 1:
#             # if total_pages == 0:
#                 print(f"Page {page}:")
#                 total_pages = response.get["total_pages",1]
#                 for user in response["data"]:
#                     if user.get("email") == email_to_check:
#                         matching_users.append({
#                         "id": user["id"],
#                     "first_name": user["first_name"],
#                         "last_name": user["last_name"]

#                     })
#             # if page >= response.get("total_pages",0):
#             #     break
           
#                 page += 1
#                 if page >total_pages:
#                     break 
#             else:
#                 break
#         #return matching_users if matching_users else "No users found with the provided email addres"
#         if matching_users:
#             # Log the action, request, and response data
#             return matching_users
#             #self.responses.append({"action": "find_user_by_email", "request": {"email": email_to_check}, "response": matching_users})
#         else:
#             return"No users found with the provided email address."
 
#     def print_stored_response(self):
#         for response_entry in self.responses:
#             print("Action:", response_entry["action"])
#             print("Request:", response_entry.get("request", ""))
#             print("Response:", response_entry.get("response", ""))

 