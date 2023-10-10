import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products =  products.fillna(int(0))
    return products
    
    
    
d = {
'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
'quantity': [32, None, None, 849],
'price': [135, 821, 9319, 3051]
}
d = pd.DataFrame(d)
print(fillMissingValues(d))