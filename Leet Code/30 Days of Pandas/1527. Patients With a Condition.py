import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains('DIAB1')]

d = {
'patient_id': [1, 2, 3, 4, 5],
'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
}

d = pd.DataFrame(d)
print(find_patients(d)) 