from user import *

def main():
    while True:
        print("Choose an action:")
        
        print("1. Get all todo details")
        print("2. Get todo data by ID")
        print("3. Get values by suite by APT")
        print("4. Get all completed True")
        print("5. Get values by Website for orgb")
        print("6. Exit")


        option = input("Enter your choice: ")
        action_mapping = {

            "1": "get_all",
            "2": "get_by_ID",
            "3" :"get_user_suite_apt",
            "4": "get_by_True",
            "5": "get_by_website_org"

        }
        if option == "6":
            break
        action = action_mapping.get(option)
        if action:
            perform_action(action)
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()