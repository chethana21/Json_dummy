from http_request import *
from action_handler import *
# class UserApp:
    
#     @classmethod
#     def main(cls):
def main():
        API_URL = "https://reqres.in/api"
        user_manager = UserManager(API_URL)
        while True:
            print("Choose an action:")
        
            print("1. Get all user details")
            print("2. Get user data by ID")
            print("3. Create user")
            print("4. Update user")
            print("5. Delete user")
            print("6. Exit")


            option = input("Enter your choice: ")

            if option == "1":
                user_data = user_manager.get_all_users_data()
                #user_data = UserManager.get_all_users_data()
                if user_data:
                    print("All User details:", user_data)
            elif option == "2":
                user_data = user_manager.get_user_data()
                if user_data:
                    print("User data:", user_data)
        
            elif option == "3":
                new_user = user_manager.create_user()
                if new_user:
                    print("New user created:", new_user)
            # elif option == "4":
            #     updated_user = update_user()
            #     if updated_user:
            #         print("User updated:", updated_user)
            # elif option == "5":
            #     deleted_user = delete_user()
            #     if deleted_user:
            #         print("User deleted:", deleted_user)
            elif option == "6":
                print("Exiting...")
                break
            else:
                user_manager.perform_action(option)
            # else:
            #     print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
    #UserApp.main()