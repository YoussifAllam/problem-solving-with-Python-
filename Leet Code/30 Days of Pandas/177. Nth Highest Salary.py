import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    data = employee['salary'].drop_duplicates()
    if N > len(data):
        d = {f'getNthHighestSalary({N})': None}
        return pd.DataFrame(d, index=[0]) 
    else:
        s = data.sort_values( ascending =  False ).iloc[N-1]
        d = {f'getNthHighestSalary({N})': s}
        return pd.DataFrame(d, index=[0])
    
    
d = {
'id': [1, 2,3],
'salary': [100, 200,300]
}
d = pd.DataFrame(d)
print(nth_highest_salary(d , 1))