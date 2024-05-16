import requests
requests.packages.urllib3.disable_warnings()
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url,verify=False)
if response.status_code == 200:
    users = response.json()
    filtered_users = []
    for user in users:
        if user['website'].endswith(".org"):
            user_data = {'id':user['id'],'name':user['name'],'company name':user['company']['name']}
            filtered_users.append(user_data)

    for user in filtered_users:
        print(user)
else:
    print("No response")