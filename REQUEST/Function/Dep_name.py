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

def find_employee_by_Dep(dep_name,employees):
    # list comp for filter & finds the employees whose dep match. Returns a list of employees details
    matching_employees =[emp for emp in employees if emp['DEPARTMENT']==dep_name]
    return matching_employees
if __name__ =='__main__':
    input_Dep=input("Enter a Deparament name: ")
    matching_employees=find_employee_by_Dep(input_Dep,employees)
    if matching_employees:
        print(f"Employees with Deparament '{input_Dep}': ")
        for emp in matching_employees:
            print(f"ID: {emp['EMPLOYEE_ID']}")
            print(f"First_Name: {emp['FIRST_NAME']}")
            print(f"Last_Name: {emp['LAST_NAME']}")
    else:
        print(f"No Match found")
