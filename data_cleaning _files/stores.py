import pandas as pd
df=pd.read_csv("Stores.csv")
#print(df)

df['Square Meters'] = df['Square Meters'].fillna(df['Square Meters'].mean())
print(df.isnull().sum())

duplicates = df.duplicated().sum()

print(duplicates)

# Convert to datetime format
df['Open Date'] = pd.to_datetime(df['Open Date'], format='%m/%d/%Y', errors='coerce')

# Extract day, month, and year
df['open day'] = df['Open Date'].dt.day
df['open month'] = df['Open Date'].dt.month
df['open year'] = df['Open Date'].dt.year

print(df)
df.drop(columns=['Open Date'], inplace=True)
print(df)
df.to_csv('stores_da.csv')
