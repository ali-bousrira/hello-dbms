import csv
import sqlite3

# Fonction pour importer les données du fichier CSV dans la table Country
def import_country_data(csv_file, db_file='CarbonFootprint.db'):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Crée la table Country si elle n'existe pas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Country (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_name TEXT NOT NULL,
            coal_usage REAL NOT NULL,
            gas_usage REAL NOT NULL,
            oil_usage REAL NOT NULL,
            hydro_usage REAL NOT NULL,
            renewable_usage REAL NOT NULL,
            nuclear_usage REAL NOT NULL
        );
        ''')

        with open(csv_file, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cursor.execute('''
                INSERT INTO Country (country_name, coal_usage, gas_usage, oil_usage, hydro_usage, renewable_usage, nuclear_usage)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['Country'],
                    float(row['Coal']),
                    float(row['Gas']),
                    float(row['Oil']),
                    float(row['Hydro']),
                    float(row['Renewable']),
                    float(row['Nuclear'])
                ))

        conn.commit()
        print("✅ Données importées avec succès dans la table 'Country'.")

    except Exception as e:
        print(f"❌ Erreur lors de l'importation des données pour Country : {e}")
    finally:
        conn.close()

# Fonction pour importer les données du fichier CSV dans la table World
def import_world_data(csv_file, db_file='CarbonFootprint.db'):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Crée la table World si elle n'existe pas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS World (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region_name TEXT NOT NULL,
            coal_usage REAL NOT NULL,
            gas_usage REAL NOT NULL,
            oil_usage REAL NOT NULL,
            hydro_usage REAL NOT NULL,
            renewable_usage REAL NOT NULL,
            nuclear_usage REAL NOT NULL
        );
        ''')

        with open(csv_file, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cursor.execute('''
                INSERT INTO World (region_name, coal_usage, gas_usage, oil_usage, hydro_usage, renewable_usage, nuclear_usage)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['Region'],
                    float(row['Coal']),
                    float(row['Gas']),
                    float(row['Oil']),
                    float(row['Hydro']),
                    float(row['Renewable']),
                    float(row['Nuclear'])
                ))

        conn.commit()
        print("✅ Données importées avec succès dans la table 'World'.")

    except Exception as e:
        print(f"❌ Erreur lors de l'importation des données pour World : {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    import_country_data('carbon-footprint-data-country.csv')
    import_world_data('carbon-footprint-data-world.csv')
