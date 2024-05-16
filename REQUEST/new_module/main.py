from action_handler import *

def main():
    while True:
        print("Choose an action:")
        
        print("1. Get all user details")
        print("2. Get user data by ID")
        print("3. Create user")
        print("4. Update user")
        print("5. Delete user")
        print("6. Exit")


        option = input("Enter your choice: ")
        action_mapping = {

            "1": "get_all",
            "2": "get",
            "3": "create",
            "4": "update",
            "5": "Delete"
        }
        action = action_mapping.get(option)
        if action:
            perform_action(action)
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
        # if option == "1":
        #     user_data = get_all_users_data()
        #     if user_data:
        #         print("All User details:", user_data)
        # if option == "2":
        #     user_data = get_user_data()
        #     if user_data:
        #         print("User data:", user_data)
        
        # elif option == "3":
        #     new_user = create_user()
        #     if new_user:
        #         print("New user created:", new_user)
        # elif option == "4":
        #     updated_user = update_user()
        #     if updated_user:
        #         print("User updated:", updated_user)
        # elif option == "5":
        #     deleted_user = delete_user()
        #     if deleted_user:
        #         print("User deleted:", deleted_user)
        # elif option == "6":
        #     print("Exiting...")
        #     break
        # else:
        #     print("Invalid option. Please choose again.")

# if __name__ == "__main__":
#     main()