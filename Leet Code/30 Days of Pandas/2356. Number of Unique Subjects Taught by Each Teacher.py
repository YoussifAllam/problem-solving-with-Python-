import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
  
  result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
  result.columns=['teacher_id','cnt']
  return result  
    
    
d = {
  'teacher_id': [1, 1, 1, 2, 2, 2, 2],
  'subject_id': [2, 2, 3, 1, 2, 3, 4],
  'dept_id': [3, 4, 3, 1, 1, 1, 1]
}

d = pd.DataFrame(d)
print(count_unique_subjects(d))