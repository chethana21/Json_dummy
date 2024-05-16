import json
from methods import *
Data_file = "new_mod_output.json"
def read_data():
    try:
        with open(Data_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def write_data(data):
    with open(Data_file, "w") as f:
        json.dump(data,f,indent=2)
def get_all_data():
    endpoint = f"users"
    return get_request(endpoint)

def get_user_data():
    user_id = input("Please enter the user ID: ")
    endpoint = f"users/{user_id}"
    return get_request(endpoint)

def create_user():
    name = input("Please enter the user's name: ")
    job = input("Please enter the user's job: ")
    endpoint = "users"
    data = {"name": name, "job": job}
    return post_request(endpoint, data)

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
    output = read_data()
    if action == "get_all":
        response = get_all_data(user_id)
    elif action == "get_id":
        user_id = input("Please enter the user ID: ")
        response = get_user_data(user_id)
    elif action == "create":
        response = create_user()
    elif action == "update":
        response = update_user()
    elif action == "Delete":
        response == delete_user()
    output.append(response)
    write_data(output)
    print("Response:", response)
def main():
    while True:
        print("Choose an option:")
        print("0. All user data")
        print("1. Get user data")
        print("2. Create user")
        print("3. Update user")
        print("4. Delete user")
        print("5. Exit")

        option = input("Enter your choice: ")
        if option == "0":
            all_user_data = get_all_data()
            if all_user_data:
                print("All Data: ",all_user_data)
        if option == "1":
            user_data = get_user_data()
            if user_data:
                print("User data:", user_data)
        elif option == "2":
            new_user = create_user()
            if new_user:
                print("New user created:", new_user)
        elif option == "3":
            updated_user = update_user()
            if updated_user:
                print("User updated:", updated_user)
        elif option == "4":
            deleted_user = delete_user()
            if deleted_user:
                print("User deleted:", deleted_user)
        elif option == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
