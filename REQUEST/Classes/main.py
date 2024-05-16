from action_handler import ActionHandler
def main():
    
    action_handler = ActionHandler("https://reqres.in/api")
    a =action_handler.get_all_user_data()
    print(a)
    b = action_handler.get_user_data(12)
    print(b)
    user_id =action_handler.create_user("Chethana","Project Engineer")
    print(user_id)
    d =action_handler.update_user(user_id, "Chowdry","Software Engineer")
    print(d)
    # e = action_handler.delete_user(user_id)
    # print(e)
    f =action_handler.find_user_by_email("tracey.ramos@reqres.in")
    print(f)
    g = action_handler.find_user_by_email("george.edwards@reqres.in")
    print(g)
if __name__ == "__main__":
    main()