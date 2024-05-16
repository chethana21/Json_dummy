from action_handler import ActionHandler

class MainProgram:
    # instance method of mainprogram 
    def __init__(self):
        self.api_url = input("Please enter the API URL: ")
        self.action_handler = ActionHandler(self.api_url)     
# creating the instance of action handler class passes api url as a parameter

    def run(self):      # run method main program loop & user interaction
        while True:
            print("Choose an action:")
            print("1. Get all user details")
            print("2. Get user data by ID")
            print("3. Create user")
            print("4. Update user")
            print("5. Delete user")
            print("6. Check email")
            print("7. Exit")

            option = input("Enter your choice: ")
            if option == "7":
                break
            # calling methods from action handler instance tp perform actions
            self.action_handler.perform_action(option)

if __name__ == "__main__":
    program = MainProgram()         # creating the instance of mainprogram
    program.run()
