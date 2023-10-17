import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
    return users[( users['mail'] .str.contains('.') | users['mail'] .str.contains('_') | users['mail'] .str.contains('-') ) & ( users['mail'] .str.contains('@leetcode.com')) ] 
    
d = {
'user_id': [1, 2, 3, 4, 5, 6, 7],
'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com']
}

d = pd.DataFrame(d)
print(valid_emails(d))