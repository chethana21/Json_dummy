import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Get_Method= requests.get('http://127.0.0.1:5000/employees/', verify=False)
print(Get_Method.json())
print(Get_Method)

id = input("Which employee id do you want to get: ")
Post_Method = requests.get(f'http://127.0.0.1:5000/employees/{id}', verify=False)
print(Post_Method.json())

id_D = input("Which employee id do you want to delete: ")
Del_Method = requests.delete(f'https://reqres.in/api/users/{id_D}', verify=False)
print(Del_Method.status_code)
print (Del_Method.headers)