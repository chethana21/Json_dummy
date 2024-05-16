import requests
requests.packages.urllib3.disable_warnings()
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url,verify=False)
if response.status_code == 200:
    users = response.json()
    user_with_apt_suite = []
    for user in users:
        address = user['address']
        if 'suite' in address and "Apt" in address['suite']:
            user_data = {'id':user['id'],'name':user['name'],'address':user['address']['city']}
            user_with_apt_suite.append(user_data)
    for user in user_with_apt_suite:
        print(user)
else:
    print("No Response")