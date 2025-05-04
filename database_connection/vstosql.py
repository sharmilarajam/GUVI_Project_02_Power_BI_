import pandas as pd
from sqlalchemy import create_engine
import pymysql           
data=pd.read_csv('product.csv',header=[0])     # Database connection details
host = "localhost"            # Replace with your MySQL server host
port = "3306"
user = "root"        # Replace with your MySQL username
password = "123456"    # Replace with your MySQL password
database = "electronics"    # Replace with the target database name

# Create a SQLAlchemy engine for the connection
#engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?auth_plugin=mysql_native_password")
#engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# Import DataFrame into MySQL table
# Replace 'your_table_name' with the name of the table you want to create/insert into
data.to_sql('products', con=engine, if_exists='replace', index=False)

print("DataFrame imported successfully!")