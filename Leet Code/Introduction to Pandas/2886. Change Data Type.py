    
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int64')
    return students
    
    
    
d = {'name': {1: 'Ava', 2: 'Kate'}, 'age': {1: 6, 2: 15}, 'grade': {1: 73.0, 2: 87.0}}
d = pd.DataFrame(d)
print(changeDatatype(d))