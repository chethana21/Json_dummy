from http_request import *
import json
OUTPUT_FILE = "TASK_2"
def read_output_file():
    try:
        with open(OUTPUT_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_output_file(output):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)
def get_all_users_data():
    endpoint = "todos"
    return get_request(endpoint)
def get_user_data():
    user_id = input("Please enter the user ID: ")
    endpoint = f"todos/{user_id}"
    return get_request(endpoint)
def get_completed_status_True():
    endpoint = "todos"
    todos = get_request(endpoint)
    if todos:
        completed_data = []
        for todo in todos:
            if todo['completed']:
                completed_task = {'userId': todo['userId'], 'id':todo['id'],'title':todo['title'],'completed':todo['completed']}
                completed_data.append(completed_task)
        return completed_data
    else:
        return None
def extract_users_with_apt_suite():
    endpoint='users'
    users = get_request(endpoint)
    if users:    
        user_with_apt_suite = []
        for user in users:
            address = user['address']
            if 'suite' in address and "Apt" in address['suite']:
                user_data = {'id':user['id'],'name':user['name'],'address':user['address']['city']}
                user_with_apt_suite.append(user_data)
        return user_with_apt_suite
       
    else:
        return None
def extract_users_with_website_org():
    endpoint = 'users'
    users = get_request(endpoint)
    if users:
        filtered_users = []
        for user in users:
            if user['website'].endswith(".org"):
                user_data = {'id':user['id'],'name':user['name'],'company name':user['company']['name']}
                filtered_users.append(user_data)
        return filtered_users       
    else:
        return None
def perform_action(action, data=None):
    output = read_output_file()
    if action == "get_all":
        response = get_all_users_data()
    elif action == "get_by_ID":
        #user_id = input("Please enter the user ID: ")
        response = get_user_data()
    elif action == "get_user_suite_apt":
        response = extract_users_with_apt_suite()
    elif action == "get_by_True":
        response = get_completed_status_True()
    elif action == "get_by_website_org":
        response = extract_users_with_website_org()
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

