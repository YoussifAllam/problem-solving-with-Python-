import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    groubs = employee.groupby(by = ['departmentId']).max()
    return groubs


 

d = {
"id": [1, 2, 3, 4, 5],
"name": ["Joe", "Jim", "Henry", "Sam", "Max"],
"salary": [70000, 90000, 80000, 60000, 90000],
"departmentId": [1, 1, 2, 2, 1]
}
d = pd.DataFrame(d)
print(department_highest_salary(d,d))