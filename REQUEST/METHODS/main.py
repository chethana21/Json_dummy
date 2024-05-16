from module import *

def get_user_details(id):
    print("enter to get_user_details function")
    key_to_data = int(input("Please enter the data to be shown from JSON dictionary: "))
    user_data = f'{api_url}/{key_to_data}'
    result=get_user_details(user_data)
    #result = get_request(user_data)
    print("Data: ", result)