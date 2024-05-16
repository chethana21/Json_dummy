import json
#PATH = 'C:\Users\Administrator\OneDrive - Wipro\Fujitsu\TASK_1\'
def write_json (data, file_path):
    try:
        with open(file_path, 'w') as file:

            json.dump(data, file, indent = 2)
            print("Data written to the JSON file")
    except Exception as e:
        print(f"Error: {e}")


#data = {'ID': 1, 'NAME': 'Chethana', 'ROLE': "Project Engineer", "Location":"CDC2"}
data = {'Person':{'ID': 1, 'NAME': 'Chethana',
        'Office' :{'ROLE': "Project Engineer", "Location":"CDC2"}}}
file_path = input("enter the path: ")
write_json(data,file_path)