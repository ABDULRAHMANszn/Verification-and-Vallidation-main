print("START")

import pyodbc

print("IMPORT DONE")

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=food_app;"
    "Trusted_Connection=yes;"
)

print("CONNECTED")