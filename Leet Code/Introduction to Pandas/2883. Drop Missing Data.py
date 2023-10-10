import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    
    return students.dropna()




data = {
    "student_id": [32, 217, 779, 849],
    "name": ["Piper", "Grace", None, None],
    "age": [5, 19, 20, 14]
}

# Create a DataFrame from the dictionary
customers = pd.DataFrame(data)
print(dropMissingData(customers))
    
    
    