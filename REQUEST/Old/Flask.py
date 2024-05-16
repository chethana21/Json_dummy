
#         {"id": 1, "name": "John Doe", "job": "Software Engineer"},
#     {"id": 2, "name": "Jane Smith", "job": "Data Scientist"},
#     {"id": 3, "name": "Michael Johnson", "job": "Project Manager"}
#     # Add more employee data here
# EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID
from flask import Flask, jsonify

app = Flask(__name__) 

# Sample employee data
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

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

 
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((emp for emp in employees if emp['EMPLOYEE_ID'] == employee_id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

 

if __name__ == '__main__':
    app.run(debug=True)

