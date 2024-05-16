employees = [
    {"EMPLOYEE_ID":112,"FIRST_NAME":"Jose Manuel","LAST_NAME":"Urman","DEPARTMENT":"FI_ACCOUNT"},
{"EMPLOYEE_ID":13,"FIRST_NAME":"Luis","LAST_NAME":"Popp","DEPARTMENT":"FI_ACCOUNT"},
{"EMPLOYEE_ID":114,"FIRST_NAME":"Den","LAST_NAME":"Raphaely","DEPARTMENT":"PU_MAN"},
{"EMPLOYEE_ID":115,"FIRST_NAME":"Alexander","LAST_NAME":"Khoo","DEPARTMENT":"PU_CLERK"},
{"EMPLOYEE_ID":116,"FIRST_NAME":"Shelli","LAST_NAME":"Baida","DEPARTMENT":"PU_CLERK"},
{"EMPLOYEE_ID":117,"FIRST_NAME":"Sigal","LAST_NAME":"Tobias","DEPARTMENT":"PU_CLERK"},
{"EMPLOYEE_ID":118,"FIRST_NAME":"Guy","LAST_NAME":"Himuro","DEPARTMENT":"PU_CLERK"},
{"EMPLOYEE_ID":119,"FIRST_NAME":"Karen","LAST_NAME":"Colmenares","DEPARTMENT":"PU_CLERK"},
{"EMPLOYEE_ID":120,"FIRST_NAME":"Matthew","LAST_NAME":"Weiss","DEPARTMENT":"ST_MAN"}
]
def get_unique_jobs_once(employees):
    dep_count = {}                              # initializing an dict to know how many time dep occurs
    for emp in employees: 
        
        # extracting the dep as as key & get is used for the count of dep title 
        # if title is not there default is 0 & increments by 1
        dep_count[emp["DEPARTMENT"]] = dep_count.get(emp["DEPARTMENT"],0)+1
    
    #iterating all the dep title creating list comp from the dep count & selects only which count is 1
    unique_jobs = [dep for dep, count in dep_count.items() if count==1]
    print("Unique Deparament Title: ")
    for dep_title in unique_jobs:
        print(dep_title)

if __name__=='__main__':
    get_unique_jobs_once(employees)

# Prints all the Deparaments once
# def get_unique_jobs():
#     unique_jobs = set(emp['DEPARTMENT'] for emp in employees)
#     return list(unique_jobs)

# if __name__=='__main__':
#     unique_jobs = get_unique_jobs()
#     print("Unique Job Title:", unique_jobs)