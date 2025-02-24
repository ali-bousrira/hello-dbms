import sqlite3

def initialize_database():
    with sqlite3.connect('CarbonFootprint.db') as conn:
        cursor = conn.cursor()
        with open('createData.sql', 'r', encoding='utf-8') as file:
            sql_script = file.read()
        cursor.executescript(sql_script)
        conn.commit()
    print("Base de données initialisée avec succès.")

if __name__ == '__main__':
    initialize_database()
