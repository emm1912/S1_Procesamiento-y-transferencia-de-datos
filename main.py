import mysql.connector as SQLC
import csv
import pandas as pd

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
    ID VARCHAR(50) PRIMARY KEY NOT NULL,                                #SE AUMENTO A 50 PORQUE LAS ID'S SON MAYORES A 24
    amount DECIMAL(24,2) NOT NULL,                                      #SE AUMENTO A 24 PORQUE HAY UN VALOR MAS LARGO QUE 16
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NULL,                                          #SE CAMBIO A NULL YA QUE LOS DATOS DE LA TABLA
    updated_at TIMESTAMP NULL,
    company_id VARCHAR(50) NOT NULL,                                    #SE AUMENTO A 50 PORQUE LAS ID'S SON MAYORES A 24
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
)
"""

create_companies_table_query = """
CREATE TABLE companies (
    company_id VARCHAR(50) PRIMARY KEY NOT NULL,
    company_name VARCHAR(130) NULL
)
"""

Cursor.execute("CREATE DATABASE Test1")
Cursor.execute("USE Test1")
print("Database Test1 has been created")
Cursor.execute(create_companies_table_query)
print("Table companies has been created")
Cursor.execute(create_charges_table_query)
print("Table charges has been created")

insert_charges_query = """
INSERT INTO charges
(ID, amount, status, created_at, updated_at, company_id)
VALUES ( %s, %s, %s, %s, %s, %s)
"""

insert_companies_query = """
INSERT INTO companies
(company_id, company_name)
VALUES ( %s, %s )
"""

file = open('data_prueba_tecnica.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)

charge_rows_new = []
charge_rows_old = []
companies_rows_new = []
companies_rows_old = []

for i, row in enumerate(csvreader):
    if bool(row):
        print(i)
        companies_rows_new = [(row[2], row[1])]
        # print(companies_rows_new[0][0])
        if companies_rows_new[0][0] not in companies_rows_old:
            Cursor.executemany(insert_companies_query, companies_rows_new)
            companies_rows_old.append(row[2])
            # print(companies_rows_old)
        if row[5] == '':
            row[5] = None
        if row[6] == '':
            row[6] = None
        charge_rows_new = [(row[0], row[3], row[4], row[5], row[6], row[2])]
        # print(charge_rows_new)
        if charge_rows_new != charge_rows_old:
            Cursor.executemany(insert_charges_query, charge_rows_new)
            charge_rows_old = [(row[0], row[3], row[4], row[5], row[6], row[2])]
        DataBase.commit()

file.close()

# select_company_query = "SELECT * FROM companies"

# df = pd.read_csv('data_prueba_tecnica.csv')
# print(df.head())
# # print(df['name'].where(df['company_id'] != "cbf1c8b09cd5b549416d49d220a40cbd317f952e"))
# df.loc[df['name'] == "MiPasajefy", ['company_id']] = 'cbf1c8b09cd5b549416d49d220a40cbd317f952e'
# # df.loc[df['paid_at'] == "", ['paid_at']] = None/
# df[['paid_at']] = df[['paid_at']].fillna(None)
# print(df)

