import json
from http_request import *

OUTPUT_FILE = "new_mod_output.json"

def read_output_file():
    try:
        with open(OUTPUT_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_output_file(output):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

def get_user_data():
    user_id = input("Please enter the user ID: ")
    endpoint = f"users/{user_id}"
    return get_request(endpoint)

    
def get_all_users_data():
    endpoint = "users"
    return get_request(endpoint)

def create_user():
    name = input("Please enter the user's name: ")
    job = input("Please enter the user's job: ")
    endpoint = "users"
    return post_request(endpoint, {"name": name, "job": job})

def update_user():
    user_id = input("Please enter the user ID to update: ")
    endpoint = f"users/{user_id}"
    data = {"name": input("Enter the new name: "), "job": input("Enter the new job: ")}
    return put_request(endpoint, data)

def delete_user():
    user_id = input("Please enter the user ID to delete: ")
    endpoint = f"users/{user_id}"
    return delete_request(endpoint)
    
def perform_action(action, data=None):
    output = read_output_file()

    if action == "get":
        #user_id = input("Please enter the user ID: ")
        response = get_user_data()
    elif action == "get_all":
        response = get_all_users_data()
    elif action == "create":
        response = create_user()
    elif action == "update":
        response = update_user()
    elif action == "Delete":
        response = delete_user()
    else:
        print("Invalid action")
        return
    response_info ={
        "action":action,
        "response" :response
    }
    #output = read_output_file()
    output.append(response_info)
    write_output_file(output)
    print("Response:", response)

