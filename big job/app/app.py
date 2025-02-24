from flask import Flask, render_template, request
import MySQLdb
import pandas as pd

app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="mdp", db="CarbonFootprint")
cursor = db.cursor()

emission_factors = {
    "coal": 820,
    "gas": 490,
    "oil": 740,
    "hydro": 24,
    "renewable": 41,
    "nuclear": 12
}

@app.route("/", methods=["GET", "POST"])
def index():
    cursor.execute("SELECT Country FROM Country")
    countries = [row[0] for row in cursor.fetchall()]

    if request.method == "POST":
        selected_country = request.form["country"]
        
        query = f"SELECT * FROM Country WHERE Country = '{selected_country}'"
        cursor.execute(query)
        country_data = cursor.fetchone()
        
        if country_data:
            country_dict = {
                "Country": country_data[1],
                "Coal": country_data[2],
                "Gas": country_data[3],
                "Oil": country_data[4],
                "Hydro": country_data[5],
                "Renewable": country_data[6],
                "Nuclear": country_data[7]
            }

            emissions = {}
            total_emission = 0
            for source, factor in emission_factors.items():
                contribution = (country_dict[f"{source}"] / 100) * factor
                emissions[source] = round(contribution, 2)
                total_emission += contribution
            
            return render_template("result.html", country=country_dict, emissions=emissions, total_emission=round(total_emission, 2))

    return render_template("index.html", countries=countries)

@app.route("/annual_emission", methods=["POST"])
def annual_emission():
    country_name = request.form["country"]
    consumption = float(request.form["consumption"])

    query = f"SELECT * FROM Country WHERE Country = '{country_name}'"
    cursor.execute(query)
    country_data = cursor.fetchone()
    
    if country_data:
        total_emission = sum((country_data[i] / 100) * factor for i, factor in enumerate(emission_factors.values(), start=2))
        annual_emission = total_emission * consumption * 8760

        return f"Les émissions annuelles pour {country_name} avec une consommation de {consumption} kWh sont de {round(annual_emission, 2)} kgCO2."

    return "Erreur lors du calcul."

if __name__ == "__main__":
    app.run(debug=True)