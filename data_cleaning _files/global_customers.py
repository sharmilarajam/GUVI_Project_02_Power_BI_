import pandas as pd
df=pd.read_csv("Customers.csv", encoding='ISO-8859-1')
print(df)
duplicates = df.duplicated().sum()
print(duplicates)
print(df.isnull().sum())
df.drop('State Code', axis=1, inplace=True)
print(df.isnull().sum())

# Convert to datetime format
df['Birthday'] = pd.to_datetime(df['Birthday'], format='%m/%d/%Y')

# Extract day, month, and year
df['b_day'] = df['Birthday'].dt.day
df['b_month'] = df['Birthday'].dt.month
df['b_year'] = df['Birthday'].dt.year

print(df)

df.drop(columns=['Birthday'], inplace=True)
print(df)

#df.to_csv('customer.csv')