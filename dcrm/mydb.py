# mydb.py

# Install MySQL Connector with:
# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server using your actual user
    dataBase = mysql.connector.connect(
        host='localhost',
        user='django_user',
        passwd='root'  # Replace with the actual password
    )

    # Check if the connection was successful
    if dataBase.is_connected():
        cursorObject = dataBase.cursor()

        # Create the database if it doesn't exist
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS django_crm_db")

        print("✅ Database 'django_crm_db' created successfully (or already exists)")

except Error as e:
    print(f"❌ Error while connecting to MySQL: {e}")

finally:
    if dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("🔌 MySQL connection closed")
