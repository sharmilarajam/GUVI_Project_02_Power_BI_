import pandas as pd 
df=pd.read_csv("Exchange_Rates.csv")
print(df)
duplicates = df.duplicated().sum()
print(duplicates)
print(df.isnull().sum())

# Convert to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Extract day, month, and year
df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year

print(df)
df.drop(columns=['Date'], inplace=True)
print(df)
df.to_csv('exchange_rate.csv')