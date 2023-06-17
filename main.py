import mysql.connector as SQLC
import csv

# Establishing connection with the SQL

DataBase = SQLC.connect(
    host="192.168.0.201",
    user="root",
    password="genesis1"
)
# Cursor to the database
Cursor = DataBase.cursor()

create_charges_table_query = """
CREATE TABLE charges (
    ID VARCHAR(24) PRIMARY KEY NOT NULL,
    amount DECIMAL(16,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    company_id VARCHAR(24) NOT NULL,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
)
"""

create_companies_table_query = """
CREATE TABLE companies (
    company_id VARCHAR(24) PRIMARY KEY NOT NULL,
    first_name VARCHAR(130) NULL
)
"""

Cursor.execute("CREATE DATABASE Test1")
Cursor.execute("USE Test1")
print("Database Test1 has been created")
Cursor.execute(create_companies_table_query)
print("Table companies has been created")
Cursor.execute(create_charges_table_query)
print("Table charges has been created")



