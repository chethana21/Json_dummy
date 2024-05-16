from action_handler import ActionHandler
def main():
    
    action_handler = ActionHandler("https://dummy.restapiexample.com/api/v1/employees")
    action_handler.get_all_users_data()
if __name__ == "__main__":
    main()