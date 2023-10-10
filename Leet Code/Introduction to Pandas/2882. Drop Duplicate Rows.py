import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])







data = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    "email": ["emily@example.com", "michael@example.com", "sarah@example.com", "john@example.com", "john@example.com", "alice@example.com"]
}

# Create a DataFrame from the dictionary
customers = pd.DataFrame(data)
print(dropDuplicateEmails(customers))
    
    
    