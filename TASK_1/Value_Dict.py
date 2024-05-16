def find_value(dictionary, key):  # find_value take a dictionary & key as arguments
    if key in dictionary:         # checks if the key exists in the dictionary using in operator
        return dictionary[key]    # keys exists it returns the corresponding value
    else:
        return None               # keys doesn't exist returns None
    #return dictionary.get(key, None) #returns the value for the given key if it exists in the dict & if not returns the defaullt value as second argument

my_dict = {'ID': 1, 'NAME': 'Chethana', 'ROLE': "Project Engineer"}

NAME_value = find_value(my_dict, 'NAME')
print(NAME_value)
ROLE_value = find_value(my_dict, 'ROLE')
print(ROLE_value)
Place_value = find_value(my_dict, 'Place')
print(Place_value)

############################################################################################################

def find_value(dictionary, key):        # find_value take a dictionary & key as arguments
    return dictionary.get(key, None)    # returns the value for the given key if it exists in the dict & if not returns the defaullt value as second argument

my_dict = {'ID': 1, 'NAME': 'Chethana', 'ROLE': "Project Engineer"}
while True:
# continuosly prompts the user to enter a key
    user_key = input("Enter a key (or 'exit'):  ")

    if user_key.lower() == 'exit':
        print("Exiting the program")
        break
    
    user_value = find_value(my_dict,user_key) # finds the value based on user input key

    if user_value is not None:
        print(f"The value for key '{user_key}' is '{user_value}',")
    else:
        print(f"The key '{user_key}' does not exist in the dictionary")