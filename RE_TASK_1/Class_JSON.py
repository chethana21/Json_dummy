import json

class JSONFileManager:
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding

    def read_json(self):
        try:
            with open(self.file_path, 'r', encoding=self.encoding) as file:
                json_data = json.load(file)
                return json_data
        except FileNotFoundError:
            return None

    def write_json(self, data):
        try:
            with open(self.file_path, 'w', encoding=self.encoding) as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
                print("Data written to the JSON file")
        except Exception as e:
            print(f"Error: {e}")

# Creating instances of the class
read_file_path = r"C:\Users\Administrator\OneDrive - Wipro\Fujitsu\RE_TASK_1\JSON_Data.json"
json_file_manager = JSONFileManager(read_file_path)

# Reading JSON
json_content = json_file_manager.read_json()
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

write_file_path = r"C:\Users\Administrator\OneDrive - Wipro\Fujitsu\RE_TASK_1\output.json"
write_json_manager = JSONFileManager(write_file_path)
write_json_manager.write_json(write_data)