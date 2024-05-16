import requests
requests.packages.urllib3.disable_warnings()
url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url,verify=False)
if response.status_code == 200:
    todos = response.json()
    completed_data = []
    #completed_todos = [todo for todo in todos if todo['completed']]
    #completed_data = [{'userId': todo['userId'], 'id':todo['id'],'title':todo['title'],'completed':todo['completed']}for todo in completed_todos]
    for todo in todos:
        if todo['completed']:
            completed_task = {'userId': todo['userId'], 'id':todo['id'],'title':todo['title'],'completed':todo['completed']}
            completed_data.append(completed_task)
    for task in completed_data:
        print(task)
        #print(todo)
else:
    print("No Data")