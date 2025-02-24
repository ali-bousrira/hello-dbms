from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

EMISSIONS = {
    "coal": 820,
    "gas": 490,
    "oil": 740,
    "hydro": 24,
    "renewable": 41,
    "nuclear": 12
}

def get_db_connection():
    try:
        conn = sqlite3.connect('CarbonFootprint.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"❌ Erreur de connexion à la base de données: {e}")
        return None

def initialize_database():
    if not os.path.exists('CarbonFootprint.db'):
        print("⚙️ Initialisation de la base de données...")
        conn = sqlite3.connect('CarbonFootprint.db')
        cursor = conn.cursor()

        if os.path.exists('createData.sql'):
            with open('createData.sql', 'r', encoding='utf-8') as file:
                sql_script = file.read()
            try:
                cursor.executescript(sql_script)
                conn.commit()
                print("✅ Base de données créée avec succès.")
            except sqlite3.Error as e:
                print(f"❌ Erreur lors de l'exécution du script SQL: {e}")
        else:
            print("❗ Fichier createData.sql introuvable. Veuillez le placer dans le même dossier.")
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if conn is None:
        return "Erreur de connexion à la base de données. Veuillez vérifier vos fichiers."

    cursor = conn.cursor()
    cursor.execute("SELECT country_name FROM Country ORDER BY country_name ASC")
    countries = [row['country_name'] for row in cursor.fetchall()]

    cursor.execute("SELECT region_name FROM World ORDER BY region_name ASC")
    regions = [row['region_name'] for row in cursor.fetchall()]

    selected_country = request.form.get("country")
    selected_region = request.form.get("region")
    consumption = float(request.form.get("consumption", 1))
    result = None

    if selected_country:
        cursor.execute("SELECT * FROM Country WHERE country_name = ?", (selected_country,))
        data = cursor.fetchone()
    elif selected_region:
        cursor.execute("SELECT * FROM World WHERE region_name = ?", (selected_region,))
        data = cursor.fetchone()
    else:
        data = None

    if data:
        usage = {
            "coal": data['coal_usage'],
            "gas": data['gas_usage'],
            "oil": data['oil_usage'],
            "hydro": data['hydro_usage'],
            "renewable": data['renewable_usage'],
            "nuclear": data['nuclear_usage']
        }

        contributions = {
            source: round((usage[source] * EMISSIONS[source]) / 100, 2) for source in usage
        }

        total_emission = round(sum(contributions.values()), 2)
        annual_emission_kg = round((total_emission / 1000) * (24 * 365) * consumption, 2)
        trees_needed = round(annual_emission_kg / 25, 2)

        result = {
            "usage": usage,
            "contributions": contributions,
            "total_emission": total_emission,
            "annual_emission_kg": annual_emission_kg,
            "trees_needed": trees_needed
        }

    conn.close()

    return render_template('index.html', 
                           countries=countries,
                           regions=regions,
                           selected_country=selected_country,
                           selected_region=selected_region,
                           result=result,
                           consumption=consumption)

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True, host='0.0.0.0', port=5000)