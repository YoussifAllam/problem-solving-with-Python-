import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts['income'] <20000])
    avg = len(accounts[ (accounts['income'] >=20000) & (accounts['income'] <=50000) ])
    high = len(accounts[ (accounts['income'] >50000)])
    
    return pd.DataFrame(
        {
          'category':[ 'Low Salary' , 'Average Salary' , 'High Salary'], 
          'accounts_count' : [low , avg , high ] 
        }
    )





d = pd.DataFrame({
'account_id': [3, 2, 8, 6],
'income': [108939, 12747, 87709, 91796]
})

print(count_salary_categories(d))