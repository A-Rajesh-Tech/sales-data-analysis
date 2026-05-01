import pandas as pd

df = pd.read_csv('../data/sales_data.csv')
df['total'] = df['price'] * df['quantity']

print(df)
print("Total Sales:", df['total'].sum())