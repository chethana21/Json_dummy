def find_keys_by_value(dictionary, value):  # find_value take a dictionary & value as arguments
    keys = []                               # created an empty list before iterating thr dict allows you to collect & store the keys are associated with a value
    for key,val in dictionary.items():
        if val == value:                    # checks the current value in the loop matches the input
            keys.append(key)                # matches adds to corresponding key to the key list
    return keys

my_dict = {'ID': 1, 'NAME': 'Chethana', 'ROLE': "Project Engineer", "Location":"CDC2","Base_Location":"CDC2"}
value_to_find = "CDC2"
keys_for_value = find_keys_by_value(my_dict, value_to_find)

print(f"The key for value '{value_to_find} are:{keys_for_value}")

##################################################################################################

# def find_keys_by_value(dictionary, value):
# #list comprehension that iterates through the dict key-value & key-value, it checks value if matches
#     return [key for key, val in dictionary.items() if val == value]

# my_dict = {'ID': 1, 'NAME': 'Chethana', 'ROLE': "Project Engineer", "Location":"CDC2"}
# while True:
# # continuosly prompts the user to enter a key
#     user_input = input("Enter a value to find keys for (or 'exit'):  ")

#     if user_input.lower() == 'exit':
#         print("Exiting the program")
#         break
    
#     keys_found = find_keys_by_value(my_dict,user_input) # finds the value based on user input key

#     if keys_found:
#         print(f"The key for value '{user_input}' is '{keys_found}',")
#     else:
#         print(f"The key '{user_input}' does not exist in the dictionary")