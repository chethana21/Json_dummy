from request import get_user_data, create_user, update_user, delete_user

def main():
    while True:
        print("Choose an option:")
        print("1. Get user data")
        print("2. Create user")
        print("3. Update user")
        print("4. Delete user")
        print("5. Exit")

        option = input("Enter your choice: ")

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
