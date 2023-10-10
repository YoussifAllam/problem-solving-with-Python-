import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']  =  employees['salary']  *2
    return employees

data = {
    "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
    "salary": [4548, 28150, 1103, 6593, 74576, 24433]
}

# Create a DataFrame from the dictionary
employees = pd.DataFrame(data)

print(modifySalaryColumn(employees))