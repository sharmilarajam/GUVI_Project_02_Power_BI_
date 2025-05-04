
import mysql.connector
from mysql.connector import Error

def check_mysql_connection(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("MySQL Server is active and accessible.")
            connection.close()
            return True
    except Error as e:
        print(f"Error: {e}")
        return False

# Replace with your actual MySQL credentials
host = "localhost"
user = "root"
password = "123456"
database = "electronics"

if check_mysql_connection(host, user, password, database):
    print("Connected successfully!")
else:
    print("Failed to connect.")
