import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivot_table = pd.pivot_table(weather, index='month', columns='city', values='temperature')
    return pivot_table
 
 
 
d = {'city': {'Jacksonville': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville'], 
              'ElPaso': ['ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso']},
 'month': {'Jacksonville': ['January', 'February', 'March', 'April', 'May'],
           'ElPaso': ['January', 'February', 'March', 'April', 'May']},
 'temperature': {'Jacksonville': [13, 23, 38, 5, 34], 'ElPaso': [20, 6, 26, 2, 43]}}

d = pd.DataFrame(d)
print(d)
#print(pivotTable(d))