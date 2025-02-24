import pandas as pd
import mysql.connector

file_path_country = "carbon-footprint-data-country.csv"
data_country = pd.read_csv(file_path_country)
file_path_world = "carbon-footprint-data-world.csv"
data_world = pd.read_csv(file_path_world)

connection = mysql.connector.connect(
    host="localhost",
    user="user",       
    password="mdp",  
    database="CarbonFootprint"
)
cursor = connection.cursor()

for _, row in data_country.iterrows():
    cursor.execute("""
        INSERT INTO Country (Country, Coal, Gas, Oil, Hydro, Renewable, Nuclear)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['Country'], row['Coal'], row['Gas'], row['Oil'], row['Hydro'], row['Renewable'], row['Nuclear']))

for _, row in data_world.iterrows():
    cursor.execute("""
        INSERT INTO World (Region, Coal, Gas, Oil, Hydro, Renewable, Nuclear)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['Region'], row['Coal'], row['Gas'], row['Oil'], row['Hydro'], row['Renewable'], row['Nuclear']))

connection.commit()
cursor.close()
connection.close()