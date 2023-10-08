import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    row  = students.query('student_id == 101')
    return row.iloc[:,1:3]

df = pd.DataFrame({'student_id': [101, 102, 103], 'name': ['Alice', 'Bob', 'Carol'], 'age': [25, 101, 35]})

print(selectData(df))