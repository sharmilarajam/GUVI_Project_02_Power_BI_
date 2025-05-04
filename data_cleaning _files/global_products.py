import pandas as pd
df=pd.read_csv("Products.csv")
print(df)
duplicates = df.duplicated().sum()
print(duplicates)
print(df.isnull().sum())
df.to_csv('product.csv')
