import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.merge_ordered(df1, df2)

df1 = pd.DataFrame({'student_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
df2 = pd.DataFrame({'student_id': [4, 5, 6], 'name': ['David', 'Eve', 'Finn'], 'age': [22, 33, 40]})
print(concatenateTables(df1 , df2 ))