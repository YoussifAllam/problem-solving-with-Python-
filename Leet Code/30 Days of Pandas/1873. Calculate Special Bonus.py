import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    result_df = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    
    return result_df
    
d = { 
'employee_id': [2, 3, 7, 8, 9],
'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
'salary': [3000, 3800, 7400, 6100, 7700]
}

d = pd.DataFrame(d)

print(calculate_special_bonus(d))