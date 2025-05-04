import pandas as pd
df=pd.read_csv("sale.csv")
print(df)
duplicates = df.duplicated().sum()

print(duplicates)
print(df.isnull().sum())
df.drop(columns=['Delivery Date'], inplace=True)
print(df.isnull().sum())

df.rename(columns={'Currency Code': 'Currency'}, inplace=True)
print(df)
# Convert to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

# Extract day, month, and year
df['Order day'] = df['Order Date'].dt.day
df['Order month'] = df['Order Date'].dt.month
df['Order year'] = df['Order Date'].dt.year
print(df)

#df.to_csv('sale.csv')
