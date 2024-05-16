import requests
import json
import urllib3
requests.packages.urllib3.disable_warnings()  
def find_details_by_name(api_url,object_name):
    response = requests.get(api_url, verify=False)
    if response.status_code == 200:
        objects = response.json()
    
    # list comp for filter & finds the models whose name match. Returns a list of phone details
        matching_name=[name for name in objects if name['name']==object_name]
        return matching_name
    else:
        print("error: ",response.status_code)
        return []

if __name__ =='__main__':
    api_url = input("Please enter the API URL: ")
    input_name=input("Enter a Phone name: ")
    matching_name=find_details_by_name(api_url,input_name)
    if matching_name:
        print(f"Phone Details by name '{input_name}': ")
        for name in matching_name:
            print(f"ID: {name['id']}")
            print(f"Phone_Name: {name['name']}")
            print(f"Data: {name['data']}")
    else:
        print(f"No Match found")

#https://api.restful-api.dev/objects