-- Création de la table Country
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

-- Création de la table World
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
