import mysql.connector as SQLC
import csv
import pandas as pd

#Loading csv into pandas and cleaning the data
df = pd.read_csv('data_prueba_tecnica.csv')                                                         #Leer archivo
df.loc[df['name'] == 'MiPasajefy', 'company_id'] = 'cbf1c8b09cd5b549416d49d220a40cbd317f952e'       #Definimos la ID de "MiPasajefy"
df.loc[df['name'] == 'Muebles chidos', 'company_id'] = '8f642dc67fccf861548dfe1c761ce22f795e91f0'   #Definimos la ID de "Muebles Chidos"
df['amount'] = df['amount'].apply(lambda x: str(x))
df['amount'] = df['amount'].str.replace('[^\d\.]','', regex=True).astype(float)                      #De columna amount solo dejamos numeros y puntos
df.dropna(subset=['id'], inplace=True)                                                               #DROPING valores vacios de columna "id"
df.to_csv('data_prueba_tecnica2.csv')

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

file = open('data_prueba_tecnica2.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)

charge_rows_new = []
charge_rows_old = []
companies_rows_new = []
companies_rows_old = []

#Sending data to MySQL
for i, row in enumerate(csvreader):
    if bool(row):
        print(i)
        companies_rows_new = [(row[3], row[2])]
        # print(companies_rows_new)
        if companies_rows_new[0][0] not in companies_rows_old:
            Cursor.executemany(insert_companies_query, companies_rows_new)
            companies_rows_old.append(row[3])
            print(companies_rows_old)
        if row[6] == '':
            row[6] = None
        if row[7] == '':
            row[7] = None
        charge_rows_new = [(row[1], row[4], row[5], row[6], row[7], row[3])]
        # print(charge_rows_new)
        if charge_rows_new != charge_rows_old:
            Cursor.executemany(insert_charges_query, charge_rows_new)
            charge_rows_old = [(row[1], row[4], row[5], row[6], row[7], row[3])]
        DataBase.commit()

file.close()


