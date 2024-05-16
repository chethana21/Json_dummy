# def find_nested_value(my_dict, key):            # 2 arguments nested dict & nested keys
#     keys = key.split('.')                       # splits the input key using dot as separators, creates a list of individual keys that make up nested path
#     value = my_dict
#     for k in keys:
#         if k in value:
#             value = value[k]
#         else:
#             return None
#     return value

# my_dict = {'Person':{'ID': 1, 'NAME': 'Chethana',
#         'Office' :{'ROLE': "Project Engineer", "Location":"CDC2"}}}

# name_value = find_nested_value(my_dict, 'Person.NAME')
# print(name_value)
# role_value = find_nested_value(my_dict, 'Person.Office.ROLE')
# print(role_value)
# Location_value = find_nested_value(my_dict, 'Person.Office.Location')
# print(Location_value)

####################################################################################################

# def find_nested_value(nested_dict, keys):
#     if not keys:                                # checks if the keys list is empty, it means it reached the deepest level of nested path
#         return nested_dict
#     first_key = keys[0]                         # extracts first key from key list which corresponds to current level of nesting
#     if first_key in nested_dict:                # checks first key exists in the nested dict
# # function calls itself recursively with next level of nested dict & remaining keys
#         return find_nested_value(nested_dict[first_key],keys[1:])
#     else:
#         return None

# my_dict = {'Person':{'ID': 1, 'NAME': 'Chethana',
#         'Office' :{'ROLE': "Project Engineer", "Location":"CDC2"}}}

# while True:
# # continuosly prompts the user to enter a key
#     user_input = input("Enter a nested key (or 'exit'):  ")

#     if user_input.lower() == 'exit':
#         print("Exiting the program")
#         break
#     user_keys = user_input.split('.')           # splits the user input into a list of keys
#     user_value = find_nested_value(my_dict,user_keys) # finds the value based on user input key

#     if user_value is not None:
#         print(f"The value for nested key '{user_input}' is '{user_value}',")
#     else:
#         print(f"The nested key '{user_input}' does not exist in the dictionary")

# def find_value_by_last_key(my_dict, key):
#     for nested_dict in my_dict.values():
#         if isinstance(nested_dict, dict) and key in nested_dict:
#             return nested_dict[key]
#     return None

 

# my_dict = {'Person': {'ID': 1, 'NAME': 'Chethana',
#                      'Office': {'ROLE': "Project Engineer", "Location": "CDC2"}}}

 

# key = 'ROLE'  # Just the last key you want to retrieve
# value = find_value_by_last_key(my_dict, key)
# print(value)

def find_value_by_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]

    for value in dictionary.values():
        if isinstance(value, dict):
            nested_value = find_value_by_key(value, key)
            if nested_value is not None:
                return nested_value

    return None

my_dict = {'Person': {'ID': 1, 'NAME': 'Chethana', 'Office': {'ROLE': "Project Engineer", "Location": "CDC2"}}}

location_value = find_value_by_key(my_dict, 'Location')
print(location_value)