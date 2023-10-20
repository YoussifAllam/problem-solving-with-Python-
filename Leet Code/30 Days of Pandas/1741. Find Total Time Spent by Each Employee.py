

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    df = employees[['event_day','emp_id', 'total_time']]
    df.columns = ['day', 'emp_id','total_time']
    return df.groupby(['day','emp_id']).sum().reset_index()