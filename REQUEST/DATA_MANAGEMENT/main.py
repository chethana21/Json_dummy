from user_management import UserManagement
def Main():
    
    action_handler = UserManagement("https://reqres.in/api")
    # a =action_handler.get_all_user_data()
    # print(a)
    # b = action_handler.get_user_data(10)
    # print(b)
    # # c = action_handler.get_user_data(4)
    # # print(c)
    user_id =action_handler.create_user("Chethana","Project Engineer")
    print(user_id)
    d =action_handler.update_user(user_id, "Chowdry","Software Engineer")
    print(d)
    # e = action_handler.delete_user(user_id)
    # print(e)
    # f =action_handler.find_user_by_email("charles.morris@reqres.in")
   # print(f)
    # g = action_handler.find_user_by_email("george.edwards@reqres.in")
    # print(g)
if __name__ == "__main__":
    Main()