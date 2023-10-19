import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        products, id_vars='product_id', var_name='store', value_name='price'
    ).dropna()
   
    
    
df = pd.DataFrame({
    'product_id': [0, 1],
    'store1': [95, 70],
    'store2': [100, None],
    'store3': [105, 80]
})

print(rearrange_products_table(df))
