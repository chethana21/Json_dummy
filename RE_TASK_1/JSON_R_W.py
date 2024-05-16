import json

def read_json_file(file_path,encoding='utf-8'):
    try:
        with open(file_path, 'r',encoding=encoding) as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        return None

def write_json(data, file_path,encoding='utf-8'):
    try:
        with open(file_path, 'w',encoding=encoding) as file:
            json.dump(data, file, indent=2,ensure_ascii=False)
            print("Data written to the JSON file")
    except Exception as e:
        print(f"Error: {e}")

# Reading JSON
read_file_path = r"C:\Users\Administrator\OneDrive - Wipro\Fujitsu\RE_TASK_1\JSON_Data.json"
json_content = read_json_file(read_file_path)

if json_content is not None:
    print("JSON Content:")
    print(json_content)
else:
    print("File not found")

# Writing JSON
write_data = {
    'Person': {
        'ID': 1,
        'NAME': 'Chethana',
        'Office': {
            'ROLE': "Project Engineer",
            "Location": "CDC2"
        }
    }
}

write_file_path = r"C:\Users\Administrator\OneDrive - Wipro\Fujitsu\RE_TASK_1\Output.json"
write_json(write_data, write_file_path)