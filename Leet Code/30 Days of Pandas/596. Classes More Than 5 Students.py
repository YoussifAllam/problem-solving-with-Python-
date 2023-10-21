import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    r = courses.groupby(['class']).count().reset_index()
    return pd.DataFrame(r[r['student']>=5]['class'])



d = {
'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}

d = pd.DataFrame(d)
print(find_classes(d))